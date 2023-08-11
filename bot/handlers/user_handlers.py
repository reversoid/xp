from typing import Text
from aiogram import Router
from aiogram.types import Message, InputMediaAudio, InputMediaDocument, InputMediaPhoto, InputMediaVideo, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.filters.callback_data import CallbackData
from lexicon.lexicon import LEXICON
from services.experiment_service import ExperimentService
from services.types import Observation
from keyboards import confirm_start_experiment_keyboard, StartExperimentCallback

router: Router = Router()

experiment_service = ExperimentService()


class NotValidObservation(Exception):
    pass


MediaGroupItem = InputMediaAudio | InputMediaDocument | InputMediaPhoto | InputMediaVideo


def observation_to_input_media(observation: Observation) -> MediaGroupItem:
    if observation.tg_photo_id:
        return InputMediaPhoto(media=observation.tg_photo_id)
    if observation.tg_document_id:
        return InputMediaDocument(media=observation.tg_document_id)
    if observation.tg_video_id:
        return InputMediaVideo(media=observation.tg_video_id)
    if observation.tg_voice_id:
        return InputMediaAudio(media=observation.tg_voice_id)
    if observation.tg_video_note_id:
        return InputMediaVideo(media=observation.tg_video_note_id)

    raise NotValidObservation


def observations_to_media_group(observations) -> list[MediaGroupItem]:
    media_group: list[MediaGroupItem] = []
    for observation in observations:
        inputMedia = observation_to_input_media(observation)
        media_group.append(inputMedia)
    return media_group


@router.message(CommandStart())
async def handle_start_command(message: Message):
    await message.answer(text=LEXICON['cmd_start'])


@router.message(Command('run_experiment'))
async def handle_start_experiment(message: Message):
    await message.answer(text=LEXICON['confirm_experiment'], reply_markup=confirm_start_experiment_keyboard)


@router.callback_query(StartExperimentCallback.filter())
async def confirm_start_experiment(query: CallbackQuery):
    if not query.from_user or not query.message or not query.message.from_user:
        await query.answer()
        return

    await query.message.edit_reply_markup(reply_markup=None)

    try:
        observations = await experiment_service.run_experiment(tg_user_id=query.message.from_user.id)
        media_group = observations_to_media_group(observations)
        await query.message.answer_media_group(media=media_group)
        await query.message.answer(LEXICON['start_experiment'])
    except:
        await query.message.answer(LEXICON['internal_error'])
    finally:
        await query.answer()
