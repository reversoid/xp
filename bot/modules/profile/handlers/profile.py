from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from modules.profile.lexicon import LEXICON
from modules.profile.keyboards.profile_keyboard import profile_keyboard
from modules.profile.services import profile_service

profile_router = Router()


@profile_router.message(Command("profile"))
async def handle_feed_command(message: Message):
    tg_user_id = message.from_user.id
    user = await profile_service.get_user(tg_user_id)

    await message.answer(
        text=f"Hello, {user.tgUsername}", reply_markup=profile_keyboard
    )
