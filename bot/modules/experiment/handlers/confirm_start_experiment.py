from datetime import datetime, timedelta
from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram import Bot
from aiogram.fsm.context import FSMContext

from modules.experiment.lexicon import LEXICON
from modules.experiment.middlewares.SchedulerMiddleware import ExperimentScheduler
from modules.experiment.utils.send_observations import send_observations
from shared.lexicon import SHARED_LEXICON
from modules.experiment.keyboards import StartExperimentCallback
from modules.experiment.services import NotEnoughObservationsException, experiment_service, AlreadyStartedExperiment
from modules.experiment.states import FSMExperiment
from shared.my_types import Observation

router: Router = Router()


@router.callback_query(StartExperimentCallback.filter())
async def confirm_start_experiment(query: CallbackQuery, bot: Bot, state: FSMContext, experiment_scheduler: ExperimentScheduler):
    try:
        observations, experiment = await experiment_service.run_experiment(tg_user_id=query.from_user.id, bot=bot)
        complete_by = datetime.fromisoformat(experiment.complete_by)

        experiment_scheduler.schedule_send_experiment_expired(
            bot, query.from_user.id, date=complete_by)

        await send_observations(bot=bot, observations=observations, user_id=query.from_user.id)

        await bot.send_message(chat_id=query.from_user.id, text=LEXICON['experiment_started'])
        await state.set_state(FSMExperiment.completing)
        await query.message.edit_reply_markup(reply_markup=None) if query.message else None

    except AlreadyStartedExperiment:
        await bot.send_message(chat_id=query.from_user.id, text=LEXICON['experiment_already_started'])
        await state.set_state(FSMExperiment.completing)

    except NotEnoughObservationsException:
        await bot.send_message(chat_id=query.from_user.id, text=LEXICON['not_enough_observations'])

    except Exception:
        await bot.send_message(chat_id=query.from_user.id, text=SHARED_LEXICON['internal_error'])

    await query.answer()
    await query.message.edit_reply_markup(reply_markup=None) if query.message else None
