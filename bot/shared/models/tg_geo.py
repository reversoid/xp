from typing import Optional
from pydantic import BaseModel

class TgGeo(BaseModel):
  longitude: float
  latitude: float
  horizontalAccuracy: Optional[int]
