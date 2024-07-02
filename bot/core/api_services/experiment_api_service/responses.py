from pydantic import BaseModel

from core.models import Experiment


class CurrentExperimentResponse:
    experiment: Experiment | None = None


class StartExperimentResponse:
    experiment: Experiment


class CompleteExperimentResponse:
    experiment: Experiment
