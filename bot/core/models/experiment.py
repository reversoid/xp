from typing import Optional
from pydantic import BaseModel
from .user import User
from .tg_geo import TgGeo
from .tg_media_group_item import TgMediaGroupItem
from datetime import datetime

class Experiment(BaseModel):
    id: str
    user: User
    tgText: Optional[str]
    tgPhotoId: Optional[str]
    tgVideoId: Optional[str]
    tgVoiceId: Optional[str]
    tgDocumentId: Optional[str]
    tgVideoNoteId: Optional[str]
    tgGeo: Optional[TgGeo]
    tgMediaGroup: list[TgMediaGroupItem]
    createdAt: datetime
    completeBy: datetime
    completedAt: Optional[datetime]
    canceledAt: Optional[datetime]
