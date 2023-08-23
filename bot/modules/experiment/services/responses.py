from pydantic import BaseModel

from shared.my_types import Experiment, Observation, UploadInfoRequest


class RandomObservationsResponse(BaseModel):
    observations: list[Observation]


class CreateExperimentRequest(UploadInfoRequest):
    text: str


class CurrentExperimentResponse:
    experiment: Experiment | None = None
