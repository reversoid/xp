from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram import Bot
from aiogram.fsm.context import FSMContext

from modules.experiment.lexicon import LEXICON
from shared.lexicon import SHARED_LEXICON
from modules.experiment.keyboards import StartExperimentCallback, confirm_start_experiment_keyboard
from modules.experiment.services import ExperimentService, experiment_service
from modules.experiment.states import FSMExperiment
from shared.types import Observation
from shared.utils.convert.observation_to_media_group import observations_to_media_group

router: Router = Router()


@router.callback_query(StartExperimentCallback.filter())
async def confirm_start_experiment(query: CallbackQuery, bot: Bot, state: FSMContext):
    try:
        observations: list[Observation] = await experiment_service.run_experiment(tg_user_id=query.from_user.id)
        media_groups = [observations_to_media_group(
            observation) for observation in observations]

        for media_group in media_groups:
            await bot.send_media_group(chat_id=query.from_user.id, media=media_group)

        await query.answer(LEXICON['experiment_started'])
        await state.set_state(FSMExperiment.completing)
        await query.message.edit_reply_markup(reply_markup=None) if query.message else None

    except Exception:
        await query.answer(SHARED_LEXICON['internal_error'])