from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from modules.auth.services import CheckUserRegistrationResponse, auth_service

from modules.profile.lexicon import LEXICON
from modules.profile.keyboards.profile_keyboard import profile_keyboard
from modules.profile.services import profile_service

profile_router = Router()


@profile_router.message(Command('profile'))
async def handle_feed_command(message: Message):
    response: CheckUserRegistrationResponse = await auth_service.is_user_registered(tg_user_id=message.from_user.id)

    await message.answer(text=f'Hello, {response.username}', reply_markup=profile_keyboard)
