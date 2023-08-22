from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from modules.experiment.lexicon import LEXICON
from modules.experiment.keyboards import confirm_start_experiment_keyboard

router: Router = Router()


@router.message(Command('run_experiment'))
async def handle_start_experiment(message: Message):
    await message.answer(text=LEXICON['confirm_experiment'], reply_markup=confirm_start_experiment_keyboard)
