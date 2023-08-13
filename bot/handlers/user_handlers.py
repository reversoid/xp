from typing import Text
from aiogram import Router
from aiogram.types import Message, InputMediaAudio, InputMediaDocument, InputMediaPhoto, InputMediaVideo, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.filters.callback_data import CallbackData
from lexicon.lexicon import LEXICON
from services import ExperimentService, ObservationService
from services.helpers import observations_to_media_group
from services.types import ObservationDTO
from keyboards import confirm_start_experiment_keyboard, StartExperimentCallback

router: Router = Router()

experiment_service = ExperimentService()
observation_service = ObservationService()

# TODO use routers for logging observation, experiments


@router.message(CommandStart())
async def handle_start_command(message: Message):
    await message.answer(text=LEXICON['cmd_start'])


@router.message(Command('help'))
async def handle_help_command(message: Message):
    await message.answer(text=LEXICON['cmd_help'])


@router.message(Command('log_observation'))
async def handle_log_observation(message: Message):
    # TODO set state for logging observation
    await message.answer(text=LEXICON['log_observation'], reply_markup=confirm_start_experiment_keyboard)


@router.message(Command('run_experiment'))
async def handle_start_experiment(message: Message):
    await message.answer(text=LEXICON['confirm_experiment'], reply_markup=confirm_start_experiment_keyboard)


@router.callback_query(StartExperimentCallback.filter())
async def confirm_start_experiment(query: CallbackQuery):
    # TODO set state for passing experiment
    await query.answer()
    await query.message.edit_reply_markup(reply_markup=None) if query.message else None


# TODO Check for state === in experiment
@router.message()
async def handle_experiment_results(message: Message):
    if message.from_user is None:
        return

    try:
        observations = await experiment_service.run_experiment(tg_user_id=message.from_user.id)
        media_group = observations_to_media_group(observations)
        await message.answer_media_group(media=media_group)
        await message.answer(LEXICON['start_experiment'])
    except Exception:
        await message.answer(LEXICON['internal_error'])

# TODO Check for state === in logging observation


@router.message()
async def handle_log_observation_results(message: Message):
    if message.from_user is None:
        return

    try:
        await observation_service.create_observation(tg_user_id=message.from_user.id, message=message)
        await message.answer(LEXICON['log_observation_success'])
    except:
        await message.answer(LEXICON['internal_error'])
