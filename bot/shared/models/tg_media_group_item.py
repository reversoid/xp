from typing import Optional
from pydantic import BaseModel

class TgMediaGroupItem(BaseModel):
  tgAudioId: Optional[str]
  tgDocumentId:  Optional[str]
  tgPhotoId: Optional[str]
  tgVideoId:  Optional[str]
