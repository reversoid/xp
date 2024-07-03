from typing import Literal
from core.models.subscription import Subscription
from pydantic import BaseModel
from core.models import Experiment, Observation, User


class ProfileResponse(BaseModel):
    user: User | None


class PaginatedObservationsResponse(BaseModel):
    cursor: str | None = None
    items: list[Observation]


class PaginatedExperimentsResponse(BaseModel):
    cursor: str | None = None
    items: list[Experiment]


class GetSubscriptionStatusResponse(BaseModel):
    status: Literal["ACTIVE", "EXPIRED", "NO_SUBSCRIPTION"]


class GetTriaResponse(BaseModel):
    subscription: Subscription
