import random
from modules.experiment.exceptions.exceptions import NoTextInExperimentResultException
from shared.api_service import ApiService, Params, Payload
from pydantic import BaseModel
from aiogram.types import Message
from aiohttp import ClientError, ClientResponseError

from shared.my_types import Experiment, Observation, UploadInfoRequest
from shared.utils.convert.message_to_upload_request import process_media_group_files, process_message_files, combine_upload_info_requests


class AlreadyStartedExperiment(Exception):
    pass


class NotStartedExperiment(Exception):
    pass


class RandomObservationsResponse(BaseModel):
    observations: list[Observation]


class CreateExperimentRequest(UploadInfoRequest):
    text: str


def get_experiment_task_id(tg_user_id: int):
    return f'experiment_user_{tg_user_id}'


class CurrentExperimentResponse:
    experiment: Experiment | None = None


class ExperimentService(ApiService):
    async def get_random_observations(self, tg_user_id: int) -> list[Observation]:
        url = f'{self.base_url}/observations/random'
        params: Params = {'amount': 3}
        headers = self.get_auth_headers(tg_user_id)
        observations: RandomObservationsResponse = await self.get(url, headers=headers, params=params, dataclass=RandomObservationsResponse)

        return observations.observations

    async def user_running_experiment(self, tg_user_id: int) -> Experiment | None:
        url = f'{self.base_url}/experiments'
        headers = self.get_auth_headers(tg_user_id)
        experiment: Experiment | None = await self.put(url, headers=headers, dataclass=Experiment)
        return experiment

    async def run_experiment(self, tg_user_id: int) -> list[Observation]:
        observations = await self.get_random_observations(tg_user_id)
        url = f'{self.base_url}/experiments'
        headers = self.get_auth_headers(tg_user_id)
        payload: Payload = {'observations_ids': [o.id for o in observations]}
        try:
            await self.put(url, headers=headers, payload=payload)
        except ClientResponseError as e:
            if e.code == 423:
                raise AlreadyStartedExperiment
            raise ClientResponseError

        return observations

    async def complete_experiment(self, tg_user_id: int, requests: list[UploadInfoRequest]):
        url = f'{self.base_url}/experiments'
        headers = self.get_auth_headers(tg_user_id)
        request: UploadInfoRequest = combine_upload_info_requests(requests=requests)
        self.__validate_complete_experiment_request(request)

        payload = request.model_dump()
        try:
            await self.patch(url, headers=headers, payload=payload)
        except ClientResponseError as e:
            if e.code == 423:
                raise NotStartedExperiment
            raise ClientResponseError

    async def cancel_experiment(self, tg_user_id: int):
        url = f'{self.base_url}/experiments'
        headers = self.get_auth_headers(tg_user_id)
        await self.delete(url, headers=headers)

    def __validate_complete_experiment_request(self, request: UploadInfoRequest):
        if not request.text:
            raise NoTextInExperimentResultException


experiment_service = ExperimentService()
