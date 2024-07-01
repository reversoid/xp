from pydantic import BaseModel
from shared.models import Observation


class GetRandomObservationsResponse(BaseModel):
    observations: list[Observation]
