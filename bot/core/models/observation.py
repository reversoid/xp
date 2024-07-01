from typing import Optional
from pydantic import BaseModel
from .user import User
from .tg_geo import TgGeo
from .tg_media_group_item import TgMediaGroupItem

class Observation(BaseModel):
    id: str
    tgText: Optional[str]
    tgPhotoId: Optional[str]
    tgVideoId: Optional[str]
    tgVoiceId: Optional[str]
    tgDocumentId: Optional[str]
    tgVideoNoteId: Optional[str]
    tgGeo: Optional[TgGeo]
    tgMediaGroup: list[TgMediaGroupItem]
    user: User
