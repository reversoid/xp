from datetime import timedelta
from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram import Bot
from aiogram.fsm.context import FSMContext

from modules.experiment.lexicon import LEXICON

from modules.experiment.services.exceptions import AlreadyStartedExperimentException
from modules.experiment.keyboards import (
    StartExperimentCallback,
)
from modules.experiment.services import (
    NotEnoughObservationsException,
    experiment_service,
)
from modules.experiment.states import FSMExperiment
from modules.root.middlewares.scheduler_middleware.scheduler import CoreScheduler
from shared.utils.send.send_observations import send_observations

router: Router = Router()


@router.callback_query(StartExperimentCallback.filter())
async def confirm_start_experiment(
    query: CallbackQuery,
    bot: Bot,
    state: FSMContext,
    scheduler: CoreScheduler,
):
    tg_user_id = query.from_user.id

    try:
        observations = await experiment_service.get_observations_for_experiment(
            tg_user_id
        )

        experiment = await experiment_service.create_experiment(
            tg_user_id=query.from_user.id
        )

        complete_by = experiment.completeBy

        async def handle_expired_experiment():
            await state.clear()
            await query.message.answer(text=LEXICON["experiment_expired"])

        async def handle_remind_experiment(time: int):
            await query.message.answer(text=LEXICON["experiment_will_expire"](time))

        scheduler.schedule_task(
            task_id=f"expired_{experiment.id}",
            callback=handle_expired_experiment,
            date=complete_by,
        )

        scheduler.schedule_task(
            task_id=f"remind_1_{experiment.id}",
            callback=lambda: handle_remind_experiment(8),
            date=complete_by - timedelta(hours=8),
        )

        scheduler.schedule_task(
            task_id=f"remind_2_{experiment.id}",
            callback=lambda: handle_remind_experiment(2),
            date=complete_by - timedelta(hours=2),
        )

        await send_observations(
            bot=bot, observations=observations, tg_user_id=query.from_user.id
        )

        await experiment_service.mark_observations_as_seen(tg_user_id, observations)

        await bot.send_message(
            chat_id=query.from_user.id,
            text=LEXICON["experiment_started"],
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
