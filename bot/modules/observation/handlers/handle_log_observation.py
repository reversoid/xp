from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from modules.core.middlewares import AlbumMiddleware
from modules.observation.lexicon import LEXICON
from modules.observation.services import observation_service
from modules.observation.services import NoDataForObservation
from modules.observation.states import FSMObservation
from shared.lexicon import SHARED_LEXICON

router: Router = Router()


@router.message(StateFilter(FSMObservation.completing), F.media_group_id == None)
async def handle_log_observation(message: Message, state: FSMContext):
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


@router.message(StateFilter(FSMObservation.completing), F.media_group_id != None)
async def handle_media_group(message: Message):
    await message.answer(text=LEXICON['send_one_item'])
