from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from modules.admin.lexicon import LEXICON

router: Router = Router()


@router.message(Command("start"))
async def cancel_experiment(
    message: Message,
):
    print("Your ID", message.from_user.id)
    await message.answer(LEXICON["command_start"])
