from shared.models import Observation, TgGeo
from shared.utils.convert.message_to_payload import process_message_files
from .exceptions import NoDataForObservation
from shared.api_service import ApiService, Payload
from aiogram.types import Message
from .dto import CreateObservationDto
from .responses import GetRandomObservationsResponse


class ObservationService(ApiService):
    async def create_observation(self, tg_user_id: int, message: Message):
        url = self.get_url("observations")
        headers = self.get_auth_headers(tg_user_id)

        dto = self.__message_to_observation_dto(message)
        self.__validate_new_observation_dto(dto)

        await self.post(url, payload=dto.model_dump(), headers=headers)

    async def get_random_observations(self, tg_user_id: int):
        url = self.get_url("observations/random")
        headers = self.get_auth_headers(tg_user_id)

        await self.get(url, headers=headers, dataclass=GetRandomObservationsResponse)

    async def mark_observation_as_viewed(self, tg_user_id: int, observation_id: str):
        url = self.get_url(f"observations/{observation_id}/views")
        headers = self.get_auth_headers(tg_user_id)

        await self.put(url, headers=headers)

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
