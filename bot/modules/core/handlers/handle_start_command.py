from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import CommandStart, StateFilter
from modules.core.lexicon import CORE_LEXICON
from aiogram.fsm.context import FSMContext


from modules.core.states import FSMRegistration
from modules.auth.services import UserExistsException, auth_service, username_pattern
from shared.lexicon import SHARED_LEXICON

start_router: Router = Router()


@start_router.message(CommandStart())
async def handle_start_command(message: Message, state: FSMContext):
    await state.clear()
    response = await auth_service.is_user_registered(message.from_user.id)

    if (response.registered):
        await message.answer(text=f'Hello, {response.username}! \n\n{CORE_LEXICON["cmd_start"]}', reply_markup=ReplyKeyboardRemove())
        # TODO check if user has running experiment
    else:
        await state.set_state(FSMRegistration.fill_username)
        await message.answer(text=CORE_LEXICON['cmd_start'], reply_markup=ReplyKeyboardRemove())
        await message.answer(text=CORE_LEXICON['fill_username'])


@start_router.message(StateFilter(FSMRegistration.fill_username), F.text.regexp(username_pattern))
async def handle_input_username(message: Message, state: FSMContext):
    try:
        await auth_service.register(message.from_user.id, message.text)
        await message.answer(text=CORE_LEXICON['welcome'])
        await state.clear()

    except UserExistsException:
        await message.answer(text=CORE_LEXICON['username_already_taken'])

    except Exception:
        await message.answer(text=SHARED_LEXICON['internal_error'])


# If wrong text of username is given
@start_router.message(StateFilter(FSMRegistration.fill_username), ~F.text.regexp(username_pattern))
async def handle_input_wrong_username(message: Message):
    await message.answer(text=CORE_LEXICON['wrong_username_format'])


# If wrong message is given
@start_router.message(StateFilter(FSMRegistration.fill_username))
async def handle_input_wrong_message(message: Message):
    await message.answer(text=CORE_LEXICON['bad_username_message'])
