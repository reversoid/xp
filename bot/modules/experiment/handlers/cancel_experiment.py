from aiogram import F, Router
from aiogram.filters import StateFilter
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from modules.experiment.lexicon import BUTTON_LEXICON, LEXICON
from modules.experiment.states import FSMExperiment
from modules.experiment.services import experiment_service, NotStartedExperimentException
from shared.lexicon import SHARED_LEXICON

router: Router = Router()


@router.message(StateFilter(FSMExperiment.completing), F.text == BUTTON_LEXICON['cancel'])
async def handle_cancel_experiment(message: Message, state: FSMContext):
    try:
        await experiment_service.cancel_experiment(message.from_user.id)
        await message.answer(text=LEXICON['cancel_experiment'], reply_markup=ReplyKeyboardRemove())

    except NotStartedExperimentException:
        await message.answer(text=LEXICON['experiment_not_started'], reply_markup=ReplyKeyboardRemove())

    except Exception:
        await message.answer(text=SHARED_LEXICON['internal_error'], reply_markup=ReplyKeyboardRemove())

    await state.clear()
