from aiogram import Router
from aiogram.filters import StateFilter, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from modules.root.middlewares.scheduler_middleware.scheduler import CoreScheduler
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


@router.message(StateFilter(FSMExperiment.completing), Command("run_experiment"))
async def complete_experiment_with_message(
    message: Message,
    state: FSMContext,
    scheduler: CoreScheduler,
):
    experiment = await experiment_service.cancel_experiment(message.from_user.id)
    scheduler.cancel_scheduled_task(task_id=f"expired_{experiment.id}")
    scheduler.cancel_scheduled_task(task_id=f"remind_1_{experiment.id}")
    scheduler.cancel_scheduled_task(task_id=f"remind_2_{experiment.id}")
    await state.clear()

    await message.answer(LEXICON["experiment_canceled"])


@router.message(StateFilter(FSMExperiment.completing))
async def complete_experiment_with_message(
    message: Message,
    state: FSMContext,
    scheduler: CoreScheduler,
    album: list[Message] = None,
):
    tg_user_id = message.from_user.id
    try:
        experiment = await experiment_service.complete_experiment(
            tg_user_id, album or [message]
        )

        scheduler.cancel_scheduled_task(task_id=f"expired_{experiment.id}")
        scheduler.cancel_scheduled_task(task_id=f"remind_1_{experiment.id}")
        scheduler.cancel_scheduled_task(task_id=f"remind_2_{experiment.id}")

        await message.answer(LEXICON["success_experiment"])
        await state.clear()
    except NotStartedExperimentException:
        await state.clear()
        await message.answer(LEXICON["experiment_not_started"])
    except NoTextInExperimentDtoException:
        await message.answer(LEXICON["no_text_in_experiment"])
