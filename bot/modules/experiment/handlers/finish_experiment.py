from aiogram import Router, F
from aiogram.types import Message

from aiogram import Router
from aiogram.filters import Command, StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from modules.experiment.keyboards import started_experiment_keyboard

from modules.experiment.lexicon import BUTTON_LEXICON, LEXICON
from modules.experiment.middlewares.SchedulerMiddleware import ExperimentScheduler
from modules.experiment.states import FSMExperiment
from modules.experiment.services import experiment_service, NoTextInExperimentResultException
from shared.lexicon import SHARED_LEXICON
from shared.my_types import UploadInfoRequest

router: Router = Router()


@router.message(StateFilter(FSMExperiment.completing), F.text == BUTTON_LEXICON['finish'])
async def handle_finish_experiment(message: Message, state: FSMContext, experiment_scheduler: ExperimentScheduler):
    data = await state.get_data()
    requests: list[UploadInfoRequest] = data.get('messages', [])
    parsed_requests = [UploadInfoRequest.model_validate(v) for v in requests]

    try:
        await experiment_service.complete_experiment(message.from_user.id, requests=parsed_requests)
        experiment_scheduler.cancel_send_experiment_expired(
            tg_user_id=message.from_user.id)
        await message.answer(text=LEXICON['success_experiment'], reply_markup=None)
        await state.clear()
    except NoTextInExperimentResultException:
        await message.answer(text=LEXICON['no_text_in_experiment'], reply_markup=started_experiment_keyboard)
    except Exception:
        await message.answer(text=SHARED_LEXICON['internal_error'], reply_markup=None)
        await state.clear()
