from aiogram.types import Message
from core.api_services.observation_api_service.dto import CreateObservationDto
from core.api_services.observation_api_service import (
    observation_api_service,
)
from core.models import TgGeo
from core.models.tg_media_group_item import TgMediaGroupItem
from .exceptions import NoDataForObservation


class ObservationService:
    def create_observation(self, tg_user_id: int, messages: list[Message]):
        dto = self.__messages_to_observation_dto(messages=messages)
        self.__validate_new_observation_dto(dto)

        return observation_api_service.create_observation(tg_user_id, dto)

    async def get_random_observations(self, tg_user_id: int, limit: int):
        observations = await observation_api_service.get_random_observations(
            tg_user_id, limit
        )
        return observations

    async def mark_observation_as_viewed(self, tg_user_id: int, observation_id: str):
        await observation_api_service.mark_observation_as_viewed(
            tg_user_id, observation_id
        )

    def __messages_to_observation_dto(
        self, messages: list[Message]
    ) -> CreateObservationDto:
        dto: CreateObservationDto

        if len(messages) == 1:
            message = messages[0]
            text = message.text or message.caption
            video_id = message.video.file_id if message.video else None
            photo_id = message.photo[-1].file_id if message.photo else None
            document_id = message.document.file_id if message.document else None
            geo = (
                TgGeo(
                    longitude=message.location.longitude,
                    latitude=message.location.latitude,
                    horizontalAccuracy=message.location.horizontal_accuracy,
                )
                if message.location
                else None
            )
            voice_id = message.voice.file_id if message.voice else None
            video_note_id = message.video_note.file_id if message.video_note else None
            dto = CreateObservationDto(
                tgText=text,
                tgPhotoId=photo_id,
                tgVideoId=video_id,
                tgDocumentId=document_id,
                tgGeo=geo,
                tgVoiceId=voice_id,
                tgVideoNoteId=video_note_id,
                tgMediaGroup=None,
            )

        else:  # For media group
            text = ""
            media_group: list[TgMediaGroupItem] = []

            for message in messages:
                text += message.text or message.caption or ""
                media_group_item = TgMediaGroupItem(
                    tgAudioId=message.audio.file_id if message.audio else None,
                    tgDocumentId=message.document.file_id if message.document else None,
                    tgPhotoId=message.photo[-1].file_id if message.photo[-1] else None,
                    tgVideoId=message.video.file_id if message.video else None,
                )
                media_group.append(media_group_item)

            dto = CreateObservationDto(tgText=text, tgMediaGroup=media_group)

        return dto

    def __validate_new_observation_dto(self, dto: CreateObservationDto):
        if (
            not dto.tgText
            and not dto.tgPhotoId
            and not dto.tgVideoId
            and not dto.tgVideoNoteId
            and not dto.tgDocumentId
            and not dto.tgGeo
            and not dto.tgMediaGroup
            and not dto.tgVoiceId
        ):
            raise NoDataForObservation


observation_service = ObservationService()
