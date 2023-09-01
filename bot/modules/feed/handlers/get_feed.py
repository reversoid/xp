from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from modules.feed.lexicon import LEXICON
from modules.feed.keyboards.feed_keyboard import feed_keyboard

feed_router = Router()


@feed_router.message(Command('feed'))
async def handle_feed_command(message: Message):
    await message.answer(text=LEXICON['feed'], reply_markup=feed_keyboard)
