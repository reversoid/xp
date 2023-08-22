from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

feed_router = Router()


@feed_router.message(Command('feed'))
async def handle_feed_command(message: Message):
    await message.answer(text='This is feed')
