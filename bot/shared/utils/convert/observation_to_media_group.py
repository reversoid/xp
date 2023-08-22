from aiogram.types import InputMediaAudio, InputMediaDocument, InputMediaPhoto, InputMediaVideo
from shared.types import Observation, ObservationDTO

MediaGroupItem = InputMediaAudio | InputMediaDocument | InputMediaPhoto | InputMediaVideo


class NotValidObservation(Exception):
    pass


def observation_to_media_group(observation: ObservationDTO) -> MediaGroupItem:
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


def observations_to_media_group(observations: list[Observation]) -> list[MediaGroupItem]:
    media_group: list[MediaGroupItem] = []
    for observation in observations:
        inputMedia = observation_to_media_group(observation)
        media_group.append(inputMedia)
    return media_group
