from pydantic import BaseModel

from shared.my_types import Experiment, Observation


class UserResponse(BaseModel):
    id: int
    tg_id: int
    username: str


class PaginatedUsersResponse(BaseModel):
    next_key: str | None = None
    items: list[UserResponse]


class PaginatedObservationsResponse(BaseModel):
    next_key: str | None = None
    items: list[Observation]


class PaginatedExperimentsResponse(BaseModel):
    next_key: str | None = None
    items: list[Experiment]
