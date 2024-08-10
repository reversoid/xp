from pydantic import BaseModel


class TgMediaGroupItem(BaseModel):
    tgAudioId: str | None = None
    tgDocumentId: str | None = None
    tgPhotoId: str | None = None
    tgVideoId: str | None = None
