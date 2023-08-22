import random
from modules.experiment.exceptions.exceptions import NoTextInExperimentResultException
from shared.api_service import ApiService, Params, Payload
from pydantic import BaseModel
from aiogram.types import Message

from shared.types import Experiment, Observation, UploadInfoRequest
from shared.utils.convert.message_to_upload_request import process_media_group_files, process_message_files


class RandomObservationsResponse(BaseModel):
    observations: list[Observation]


class CreateExperimentRequest(UploadInfoRequest):
    text: str


def get_experiment_task_id(tg_user_id: int):
    return f'experiment_user_{tg_user_id}'


class ExperimentService(ApiService):
    async def get_random_observations(self, tg_user_id: int) -> list[Observation]:
        url = f'{self.base_url}/observation/random'
        params: Params = {'amount': 3}
        headers = self.get_auth_headers(tg_user_id)
        observations: RandomObservationsResponse = await self.put(url, headers=headers, params=params, dataclass=RandomObservationsResponse)
        return observations.observations

    async def user_running_experiment(self, tg_user_id: int) -> Experiment | None:
        # TODO make proper request
        return random.choice([Experiment(id=666), None])

    async def run_experiment(self, tg_user_id: int) -> list[Observation]:
        observations = await self.get_random_observations(tg_user_id)
        url = f'{self.base_url}/experiment'
        headers = self.get_auth_headers(tg_user_id)
        payload: Payload = {'observations_ids': [o.id for o in observations]}
        await self.put(url, headers=headers, payload=payload)
        return observations

    async def complete_experiment(self, tg_user_id: int, message: Message | list[Message]):
        url = f'{self.base_url}/experiment'
        headers = self.get_auth_headers(tg_user_id)
        request: UploadInfoRequest = process_media_group_files(
            message) if isinstance(message, list) else process_message_files(message)
        self.__validate_complete_experiment_request(request)

        payload = request.model_dump()
        await self.patch(url, headers=headers, payload=payload)

    def __validate_complete_experiment_request(self, request: UploadInfoRequest):
        if not request.text:
            raise NoTextInExperimentResultException

experiment_service = ExperimentService()