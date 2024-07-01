from core.models import TgGeo, TgMediaGroupItem
from pydantic import BaseModel


class CreateObservationDto(BaseModel):
    tgText: str | None
    tgPhotoId: str | None
    tgVideoId: str | None
    tgVoiceId: str | None
    tgDocumentId: str | None
    tgVideoNoteId: str | None
    tgGeo: TgGeo | None
    tgMediaGroup: list[TgMediaGroupItem] | None
