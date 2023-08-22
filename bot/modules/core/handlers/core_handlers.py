from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart, StateFilter
from modules.core.lexicon import CORE_LEXICON
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state


from modules.core.states import FSMRegistration
from modules.auth.services import auth_service

core_router: Router = Router()


@core_router.message(CommandStart())
async def handle_start_command(message: Message, state: FSMContext):
    response = await auth_service.is_user_registered(message.from_user.id)

    if (response.registered):
        await message.answer(text=CORE_LEXICON['cmd_start'])
        await message.answer('Welcome back! User...123')
    else:
        await state.set_state(FSMRegistration.fill_username)
        await message.answer(text=CORE_LEXICON['cmd_start'])
        await message.answer('Please input a username')

    # TODO welcome user or ask to fill username
    # context.set_state(FSMRegistration)


@core_router.message(StateFilter(FSMRegistration.fill_username), F.text.isalpha())
async def handle_input_username(message: Message, state: FSMContext):
    await auth_service.register(message.from_user.id, message.text or 'tg:' + str(message.from_user.id))
    await state.clear()


@core_router.message(Command('help'))
async def handle_help_command(message: Message):
    await message.answer(text=CORE_LEXICON['cmd_help'])


@core_router.message()
async def no_understand(message: Message):
    await message.answer(text=CORE_LEXICON['cannot_undertand'])
