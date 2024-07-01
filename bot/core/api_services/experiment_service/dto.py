from pydantic import BaseModel
from shared.models import TgGeo, TgMediaGroupItem


class CompleteExperimentDto(BaseModel):
    tgText: str
    tgPhotoId: str | None
    tgVideoId: str | None
    tgVoiceId: str | None
    tgDocumentId: str | None
    tgVideoNoteId: str | None
    tgGeo: TgGeo | None
    tgMediaGroup: list[TgMediaGroupItem] | None
