from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from shared.middlewares.album_middleware import AlbumMiddleware

from modules.experiment.lexicon import LEXICON
from modules.experiment.states import FSMExperiment
from modules.experiment.services import (
    experiment_service,
    NoTextInExperimentDtoException,
    NotStartedExperimentException,
)

router: Router = Router()

router.message.middleware.register(AlbumMiddleware())


@router.message(StateFilter(FSMExperiment.completing))
async def complete_experiment_with_message(
    message: Message, state: FSMContext, album: list[Message]
):
    tg_user_id = message.from_user.id
    try:
        await experiment_service.complete_experiment(tg_user_id, album or [message])
        await message.answer(LEXICON["success_experiment"])
        await state.clear()
    except NotStartedExperimentException:
        await state.clear()
        await message.answer(LEXICON["experiment_not_started"])
    except NoTextInExperimentDtoException:
        await message.answer(LEXICON["no_text_in_experiment"])
