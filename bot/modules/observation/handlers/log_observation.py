from aiogram import Router
from aiogram.filters import Command, StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from modules.observation.lexicon import LEXICON
from modules.observation.services import ObservationService, observation_service
from modules.observation.services import NoDataForObservation
from modules.observation.states import FSMObservation
from modules.experiment.keyboards import confirm_start_experiment_keyboard
from shared.lexicon import SHARED_LEXICON

router: Router = Router()


@router.message(Command('log_observation'))
async def handle_log_observation(message: Message, state: FSMContext):
    await state.set_state(FSMObservation.completing)
    await message.answer(text=LEXICON['log_observation'])


# TODO need any filters?
@router.message(StateFilter(FSMObservation.completing))
async def handle_log_observation_results(message: Message, state: FSMContext):
    if message.from_user is None:
        return

    try:
        await observation_service.create_observation(tg_user_id=message.from_user.id, message=message)
        await message.answer(LEXICON['log_observation_success'])
        await state.clear()

    except NoDataForObservation:
        await message.answer(LEXICON['not_supported_data'])

    except Exception as e:
        await state.clear()
        await message.answer(SHARED_LEXICON['internal_error'])
