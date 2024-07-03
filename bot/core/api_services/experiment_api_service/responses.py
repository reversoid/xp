from pydantic import BaseModel

from core.models import Experiment


class CurrentExperimentResponse(BaseModel):
    experiment: Experiment | None = None


class StartExperimentResponse(BaseModel):
    experiment: Experiment


class CompleteExperimentResponse(BaseModel):
    experiment: Experiment
