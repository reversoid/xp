from pydantic import BaseModel
from core.models import Observation


class GetRandomObservationsResponse(BaseModel):
    observations: list[Observation]
