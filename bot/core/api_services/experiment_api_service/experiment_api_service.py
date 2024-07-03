from .exceptions import AlreadyStartedExperimentException, NoActiveExperimentException
from .responses import (
    CurrentExperimentResponse,
    StartExperimentResponse,
    CompleteExperimentResponse,
)
from core.api_services.utils.api_service import ApiException, ApiService
from core.models import Experiment
from .dto import CompleteExperimentDto


class ExperimentApiService(ApiService):

    async def get_user_current_experiment(self, tg_user_id: int) -> Experiment | None:
        url = f"{self.base_url}/experiments"
        headers = self.get_auth_headers(tg_user_id)
        response: CurrentExperimentResponse = await self.get(
            url, headers=headers, dataclass=CurrentExperimentResponse
        )
        return response.experiment

    async def complete_experiment(
        self, tg_user_id: int, dto: CompleteExperimentDto
    ) -> Experiment:
        url = f"{self.base_url}/experiments"
        headers = self.get_auth_headers(tg_user_id)
        payload = dto.model_dump()

        try:
            response: CompleteExperimentResponse = await self.patch(
                url,
                headers=headers,
                dataclass=CompleteExperimentResponse,
                payload=payload,
            )
            return response.experiment
        except ApiException as e:
            if e.message == "NO_ACTIVE_EXPERIMENT":
                raise NoActiveExperimentException
            raise e

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
                raise AlreadyStartedExperimentException
            raise e


experiment_api_service = ExperimentApiService()
