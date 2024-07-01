from aiogram.types import Message
from core.api_services.observation_service.dto import CreateObservationDto
from core.api_services.observation_service import observation_service as api_service
from core.models import TgGeo
from .exceptions import NoDataForObservation


class ObservationService:
    def create_observation(self, tg_user_id: int, message: Message):
        dto = self.__message_to_observation_dto(message=message)
        self.__validate_new_observation_dto(dto)

        return api_service.create_observation(tg_user_id, dto)

    def get_random_observations(self, tg_user_id: int):
        return api_service.get_random_observations(tg_user_id)

    async def mark_observation_as_viewed(self, tg_user_id: int, observation_id: str):
        await api_service.mark_observation_as_viewed(tg_user_id, observation_id)

    def __message_to_observation_dto(self, message: Message) -> CreateObservationDto:
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

        observation = CreateObservationDto(
            tgText=text,
            tgDocumentId=document_id,
            tgGeo=geo,
            tgPhotoId=photo_id,
            tgVideoId=video_id,
            tgVoiceId=voice_id,
            tgVideoNoteId=video_note_id,
            tgMediaGroup=None,
        )

        return observation

    def __validate_new_observation_dto(self, dto: CreateObservationDto):
        if (
            not dto.tgText
            and not dto.tgPhotoId
            and not dto.tgVideoId
            and not dto.tgVideoId
            and not dto.tgVideoNoteId
            and not dto.tgDocumentId
            and not dto.tgGeo
        ):
            raise NoDataForObservation


observation_service = ObservationService()
