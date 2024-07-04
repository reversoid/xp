from core.models import TgGeo, TgMediaGroupItem
from pydantic import BaseModel


class CreateObservationDto(BaseModel):
    tgText: str | None = None
    tgPhotoId: str | None = None
    tgVideoId: str | None = None
    tgVoiceId: str | None = None
    tgDocumentId: str | None = None
    tgVideoNoteId: str | None = None
    tgGeo: TgGeo | None = None
    tgMediaGroup: list[TgMediaGroupItem] | None = None
