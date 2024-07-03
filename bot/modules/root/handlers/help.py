from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from modules.root.lexicon import CORE_LEXICON


help_router: Router = Router()


@help_router.message(Command("help"))
async def handle_help_command(message: Message):
    await message.answer(text=CORE_LEXICON["cmd_help"])
