from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message
from modules.profile.lexicon import LEXICON
from aiogram.fsm.context import FSMContext
from modules.profile.services import profile_service, NoSuchUserException, AlreadySubscribedException

from modules.profile.states import FSMProfile
from shared.lexicon import SHARED_LEXICON

follow_router = Router()


@follow_router.message(Command('follow'))
async def handle_follow_command(message: Message, state: FSMContext):
    await state.set_state(FSMProfile.sending_username_to_follow)
    await message.answer(text=LEXICON['send_username'])


@follow_router.message(StateFilter(FSMProfile.sending_username_to_follow), F.text)
async def handle_input_username(message: Message, state: FSMContext):
    try:
        await profile_service.follow_user_by_username(message.from_user.id, message.text)
        await state.clear()
        await message.answer(text=LEXICON['followed_successfully'])
    except NoSuchUserException:
        await message.answer(text=LEXICON['no_such_user'])
    except AlreadySubscribedException:
        await message.answer(text=LEXICON['already_subscribed'])
    except Exception as e:
        print(e)
        await message.answer(text=SHARED_LEXICON['internal_error'])


@follow_router.message(StateFilter(FSMProfile.sending_username_to_follow), ~F.text)
async def handle_input_wrong_username(message: Message):
    await message.answer(text=LEXICON['no_username_provided'])