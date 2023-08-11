from pydantic import BaseModel
from typing import Optional


class MediaGroupItem(BaseModel):
    audio_id: Optional[str] = None
    document_id: Optional[str] = None
    photo_id: Optional[str] = None
    video_id: Optional[str] = None


class Observation(BaseModel):
    text: Optional[str]
    tg_photo_id: Optional[str]
    tg_document_id: Optional[str]
    tg_voice_id: Optional[str]
    tg_video_id: Optional[str]
    tg_video_note_id: Optional[str]
    file_urls: Optional[list[str]]
    tg_media_group: Optional[list[MediaGroupItem]]


class Geo(BaseModel):
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
    media_group: list[MediaGroupItem] | None = None
    geo: Optional[Geo] = None
