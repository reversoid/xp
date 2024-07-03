from datetime import datetime
from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram import Bot
from aiogram.fsm.context import FSMContext

from modules.experiment.lexicon import LEXICON
from modules.experiment.middlewares.SchedulerMiddleware import ExperimentScheduler
from modules.experiment.services.exceptions import AlreadyStartedExperimentException
from modules.experiment.keyboards import (
    StartExperimentCallback,
    started_experiment_keyboard,
)
from modules.experiment.services import (
    NotEnoughObservationsException,
    experiment_service,
)
from modules.experiment.states import FSMExperiment
from shared.utils.send.send_observations import send_observations

router: Router = Router()


@router.callback_query(StartExperimentCallback.filter())
async def confirm_start_experiment(
    query: CallbackQuery,
    bot: Bot,
    state: FSMContext,
    experiment_scheduler: ExperimentScheduler,
):
    tg_user_id = query.from_user.id

    try:
        observations = await experiment_service.get_observations_for_experiment(
            tg_user_id
        )

        experiment = await experiment_service.create_experiment(
            tg_user_id=query.from_user.id
        )

        complete_by = datetime.fromisoformat(experiment.completeBy)

        experiment_scheduler.schedule_send_experiment_expired(
            bot, query.from_user.id, date=complete_by
        )

        await send_observations(
            bot=bot, observations=observations, tg_user_id=query.from_user.id
        )

        await experiment_service.mark_observations_as_seen(observations)

        await bot.send_message(
            chat_id=query.from_user.id,
            text=LEXICON["experiment_started"],
            reply_markup=started_experiment_keyboard,
        )

        await state.set_state(FSMExperiment.completing)
        if query.message:
            query.message.edit_reply_markup(reply_markup=None)

        await query.answer()

    except AlreadyStartedExperimentException:
        await bot.send_message(
            chat_id=query.from_user.id, text=LEXICON["experiment_already_started"]
        )
        await state.set_state(FSMExperiment.completing)
        await query.answer()

    except NotEnoughObservationsException:
        await bot.send_message(
            chat_id=query.from_user.id, text=LEXICON["not_enough_observations"]
        )
        await state.clear()
        await query.answer()

    await query.message.edit_reply_markup(reply_markup=None) if query.message else None
