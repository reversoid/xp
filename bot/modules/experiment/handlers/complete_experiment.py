from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from modules.core.middlewares.AlbumMiddleware import AlbumMiddleware

from modules.experiment.lexicon import LEXICON
from modules.experiment.states import FSMExperiment
from modules.experiment.services import (
    experiment_service,
    NoTextInExperimentDtoException,
    NotStartedExperimentException,
)

router: Router = Router()

router.message.middleware.register(AlbumMiddleware())


@router.message(StateFilter(FSMExperiment.completing), F.media_group_id == None)
async def complete_experiment_with_message(message: Message, state: FSMContext):
    tg_user_id = message.from_user.id
    try:
        await experiment_service.complete_experiment(tg_user_id, [message])
        await message.answer(LEXICON["success_experiment"])
        await state.clear()
    except NotStartedExperimentException:
        await state.clear()
        await message.answer(LEXICON["experiment_not_started"])
    except NoTextInExperimentDtoException:
        await message.answer(LEXICON["no_text_in_experiment"])


@router.message(StateFilter(FSMExperiment.completing), F.media_group_id != None)
async def complete_experiment_with_media_group(
    message: Message, state: FSMContext, album: list[Message]
):
    tg_user_id = message.from_user.id
    try:
        await experiment_service.complete_experiment(tg_user_id, album)
        await message.answer(LEXICON["success_experiment"])
        await state.clear()
    except NotStartedExperimentException:
        await state.clear()
        await message.answer(LEXICON["experiment_not_started"])
    except NoTextInExperimentDtoException:
        await message.answer(LEXICON["no_text_in_experiment"])
