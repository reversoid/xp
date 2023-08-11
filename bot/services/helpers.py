from .types import Observation
from aiogram.types import InputMediaAudio, InputMediaDocument, InputMediaPhoto, InputMediaVideo

MediaGroupItem = InputMediaAudio | InputMediaDocument | InputMediaPhoto | InputMediaVideo


class NotValidObservation(Exception):
    pass


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
