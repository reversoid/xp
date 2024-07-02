from modules.experiment.exceptions.exceptions import NoTextInExperimentResultException
from .exceptions import (
    AlreadyStartedExperiment,
)
from .responses import CurrentExperimentResponse, StartExperimentResponse
from shared.api_service import ApiException, ApiService, Params, Payload

from core.models import Experiment


class ExperimentService(ApiService):

    async def get_user_current_experiment(self, tg_user_id: int) -> Experiment | None:
        url = f"{self.base_url}/experiments"
        headers = self.get_auth_headers(tg_user_id)
        response: CurrentExperimentResponse = await self.get(
            url, headers=headers, dataclass=CurrentExperimentResponse
        )
        return response.experiment

    async def start_experiment(self, tg_user_id: int) -> Experiment:
        url = f"{self.base_url}/experiments"
        headers = self.get_auth_headers(tg_user_id)
        try:
            response: StartExperimentResponse = await self.put(
                url, headers=headers, dataclass=StartExperimentResponse
            )
            return response.experiment
        except ApiException as e:
            if e.message == "ALREADY_STARTED_EXPERIMENT":
                raise AlreadyStartedExperiment
            raise e


experiment_service = ExperimentService()
