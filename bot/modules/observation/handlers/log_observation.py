from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from modules.observation.lexicon import LEXICON
from modules.observation.states import FSMObservation
from shared.lexicon import SHARED_LEXICON

router: Router = Router()

# TODO check payment


@router.message(Command("log_observation"))
async def handle_log_observation(message: Message, state: FSMContext):
    await state.set_state(FSMObservation.completing)
    await message.answer(text=LEXICON["log_observation"])


@router.message(Command("cancel"))
async def handle_cancel_log_observation(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(text=SHARED_LEXICON["ok"])
