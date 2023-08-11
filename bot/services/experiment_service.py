from .exceptions import NoTextInExperimentResultException
from .api_service import ApiService, Payload, Params
from pydantic import BaseModel
from .types import Observation, UploadInfoRequest
from aiogram.types import Message
from .utils import process_message_files, process_media_group_files


class RandomObservationsResponse(BaseModel):
    observations: list[Observation]


class CreateExperimentRequest(UploadInfoRequest):
    text: str


class ExperimentService(ApiService):
    async def get_random_observations(self, tg_user_id: int) -> list[Observation]:
        url = f'{self.base_url}/observation/random'
        params: Params = {'amount': 3}
        headers = self.get_auth_headers(tg_user_id)
        observations: RandomObservationsResponse = await self.put(url, headers=headers, params=params, dataclass=RandomObservationsResponse)
        return observations.observations

    async def run_experiment(self, tg_user_id: int):
        observations = await self.get_random_observations(tg_user_id)
        url = f'{self.base_url}/experiment'
        headers = self.get_auth_headers(tg_user_id)
        await self.put(url, headers=headers)
        return observations

    async def complete_experiment(self, tg_user_id: int, message: Message | list[Message]):
        url = f'{self.base_url}/experiment'
        headers = self.get_auth_headers(tg_user_id)
        request: UploadInfoRequest = process_media_group_files(
            message) if isinstance(message, list) else process_message_files(message)
        self.__validate_complete_experiment_request(request)

        payload = request.dict()
        await self.patch(url, headers=headers, payload=payload)

    def __validate_complete_experiment_request(self, request: UploadInfoRequest):
        if not request.text:
            raise NoTextInExperimentResultException
