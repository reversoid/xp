from aiogram import Router
from aiogram.filters import Command, StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from modules.core.middlewares.AlbumMiddleware import AlbumMiddleware
from modules.observation.lexicon import LEXICON
from modules.observation.services import observation_service
from modules.observation.services import NoDataForObservation
from modules.observation.states import FSMObservation

router: Router = Router()


@router.message(Command('log_observation'))
async def handle_log_observation(message: Message, state: FSMContext):
    await state.set_state(FSMObservation.completing)
    await message.answer(text=LEXICON['log_observation'])
