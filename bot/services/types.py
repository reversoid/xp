from pydantic import BaseModel
from typing import Optional


class MediaGroupItemDTO(BaseModel):
    audio_id: Optional[str] = None
    document_id: Optional[str] = None
    photo_id: Optional[str] = None
    video_id: Optional[str] = None


class ObservationDTO(BaseModel):
    text: Optional[str]
    tg_photo_id: Optional[str]
    tg_document_id: Optional[str]
    tg_voice_id: Optional[str]
    tg_video_id: Optional[str]
    tg_video_note_id: Optional[str]
    file_urls: Optional[list[str]]
    tg_media_group: Optional[list[MediaGroupItemDTO]]


class Observation(ObservationDTO):
    id: int


class GeoDTO(BaseModel):
    longitude: float
    latitude: float
    horizontal_accuracy: Optional[float]


class UploadInfoRequest(BaseModel):
    text: str | None = None
    photo_id: str | None = None
    document_id: str | None = None
    voice_id: str | None = None
    video_id: str | None = None
    video_note_id: str | None = None
    media_group: list[MediaGroupItemDTO] | None = None
    geo: Optional[GeoDTO] = None
