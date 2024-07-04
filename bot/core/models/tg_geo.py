from pydantic import BaseModel


class TgGeo(BaseModel):
    longitude: float
    latitude: float
    horizontalAccuracy: int | None = None
