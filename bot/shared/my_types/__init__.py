from pydantic import BaseModel
from typing import Optional
from aiogram.types import InputMediaAudio, InputMediaDocument, InputMediaPhoto, InputMediaVideo

MediaGroupItem = InputMediaAudio | InputMediaDocument | InputMediaPhoto | InputMediaVideo


class MediaGroupItemDTO(BaseModel):
    audio_id: Optional[str] = None
    document_id: Optional[str] = None
    photo_id: Optional[str] = None
    video_id: Optional[str] = None


class ObservationDTO(BaseModel):
    text: Optional[str] = None
    tg_photo_id: Optional[str] = None
    tg_document_id: Optional[str] = None
    tg_voice_id: Optional[str] = None
    tg_video_id: Optional[str] = None
    tg_video_note_id: Optional[str] = None
    file_urls: Optional[list[str]] = None
    tg_media_group: Optional[list[MediaGroupItemDTO]] = None


class Observation(ObservationDTO):
    id: int


class GeoDTO(BaseModel):
    longitude: float
    latitude: float
    horizontal_accuracy: Optional[float] = None


class UploadInfoRequest(BaseModel):
    text: str | None = None
    photo_id: str | None = None
    document_id: str | None = None
    voice_id: str | None = None
    video_id: str | None = None
    video_note_id: str | None = None
    media_group: list[MediaGroupItemDTO] | None = None
    geo: Optional[GeoDTO] = None


class User(BaseModel):
    id: int


class Experiment(BaseModel):
    id: int
    text: str | None = None
    complete_by: str | None = None
    tg_photo_id: Optional[str] = None
    tg_document_id: Optional[str] = None
    tg_voice_id: Optional[str] = None
    tg_video_id: Optional[str] = None
    tg_video_note_id: Optional[str] = None
    file_urls: Optional[list[str]] = None
    tg_media_group: Optional[list[MediaGroupItemDTO]] = None
    user: User | None = None
