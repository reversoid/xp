from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from modules.profile.lexicon import LEXICON

profile_router = Router()


@profile_router.message(Command('profile'))
async def handle_feed_command(message: Message):
    await message.answer(text=LEXICON['about_profile_command'])
