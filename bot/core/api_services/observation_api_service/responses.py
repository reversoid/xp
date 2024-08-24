from core.api_services.profile_api_service.responses import PaginatedObservations
from pydantic import BaseModel
from core.models import Observation


class GetRandomObservationsResponse(BaseModel):
    observations: list[Observation]


# TODO make paginatedObservations import from shared
class GetWaitlistObservationsResponse(BaseModel):
    observations: PaginatedObservations


class WaitlistAmountResponse(BaseModel):
    amount: int
