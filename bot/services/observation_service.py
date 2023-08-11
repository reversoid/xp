from typing import Optional, Union
from .api_service import ApiService, Payload
from aiogram.types import Message
from dataclasses import dataclass
from pydantic import BaseModel


@dataclass
class MediaGroupDTO(BaseModel):
    audio_id: Optional[str] = None
    document_id: Optional[str] = None
    photo_id: Optional[str] = None
    video_id: Optional[str] = None


@dataclass
class CreateObservationRequest(BaseModel):
    text: str | None = None
    photo_id: str | None = None
    document_id: str | None = None
    voice_id: str | None = None
    video_id: str | None = None
    video_note_id: str | None = None
    media_group: list[MediaGroupDTO] | None = None


class ObservationService(ApiService):
    async def create_observation(self, tg_user_id: int, message: Union[Message, list[Message]]):
        url = f'{self.base_url}/observation'
        request = self.__process_media_group(message) if isinstance(
            message, list) else self.__process_one_message(message)
        headers = self.get_auth_headers(tg_user_id)
        await self.post(url, payload=request, headers=headers)

    def __process_media_group(self, messages: list[Message]) -> Payload:
        text = ''
        media_group: list[MediaGroupDTO] = []
        for message in messages:
            if message.text:
                text = f'{text} {message.text}'
            if message.caption:
                text = f'{text} {message.caption}'
            audio_id = message.audio.file_id if message.audio else None
            document_id = message.document.file_id if message.document else None
            photo_id = message.photo[-1].file_id if message.photo else None
            video_id = message.video.file_id if message.video else None
            media_group_item = MediaGroupDTO(
                audio_id=audio_id, document_id=document_id, photo_id=photo_id, video_id=video_id)
            media_group.append(media_group_item)
        request = CreateObservationRequest(
            text=text if text else None, media_group=media_group)
        return request.dict()

    def __process_one_message(self, message: Message) -> Payload:
        document_id = message.document.file_id if message.document else None
        text = message.text
        photo_id = message.photo[-1].file_id if message.photo else None
        video_id = message.video.file_id if message.video else None
        video_note_id = message.video_note.file_id if message.video_note else None
        voice_id = message.voice.file_id if message.voice else None

        request = CreateObservationRequest(
            document_id=document_id, text=text, photo_id=photo_id, video_id=video_id, video_note_id=video_note_id, voice_id=voice_id)

        return request.dict()
