from pydantic import BaseModel

from shared.models import Experiment, Observation


class CurrentExperimentResponse:
    experiment: Experiment | None = None
