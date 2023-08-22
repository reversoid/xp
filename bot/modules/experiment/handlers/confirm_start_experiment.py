from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram import Bot
from aiogram.fsm.context import FSMContext

from modules.experiment.lexicon import LEXICON
from shared.lexicon import SHARED_LEXICON
from modules.experiment.keyboards import StartExperimentCallback, confirm_start_experiment_keyboard
from modules.experiment.services import ExperimentService, experiment_service, AlreadyStartedExperiment
from modules.experiment.states import FSMExperiment
from shared.my_types import Observation
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

    except AlreadyStartedExperiment:
        await query.answer(LEXICON['experiment_already_started'])
        await state.set_state(FSMExperiment.completing)
        

    except Exception as e:
        print(e)
        await query.answer(SHARED_LEXICON['internal_error'])
