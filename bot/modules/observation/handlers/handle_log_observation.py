from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from modules.root.middlewares.AlbumMiddleware import AlbumMiddleware
from modules.observation.lexicon import LEXICON
from modules.observation.services import observation_service
from modules.observation.services import NoDataForObservation
from modules.observation.states import FSMObservation

router: Router = Router()

router.message.middleware.register(AlbumMiddleware())


@router.message(StateFilter(FSMObservation.completing))
async def handle_log_observation(
    message: Message, state: FSMContext, album: list[Message] = None
):
    try:
        await observation_service.create_observation(
            tg_user_id=message.from_user.id, messages=album or [message]
        )
        await message.answer(LEXICON["log_observation_success"])
        await state.clear()

    except NoDataForObservation:
        await message.answer(LEXICON["not_supported_data"])
