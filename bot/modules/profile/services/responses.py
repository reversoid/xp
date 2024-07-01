from pydantic import BaseModel
from shared.models import Experiment, Observation, User


class ProfileResponse(BaseModel):
    user: User


class PaginatedObservationsResponse(BaseModel):
    cursor: str | None = None
    items: list[Observation]


class PaginatedExperimentsResponse(BaseModel):
    cursor: str | None = None
    items: list[Experiment]
