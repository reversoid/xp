from datetime import datetime, timedelta
from aiogram import Bot
from modules.experiment.exceptions.exceptions import NoTextInExperimentResultException
from modules.experiment.services.exceptions import AlreadyStartedExperiment, NotEnoughObservationsException, NotStartedExperimentException
from modules.experiment.services.responses import RandomObservationsResponse
from shared.api_service import ApiService, Params, Payload
from aiohttp import ClientResponseError

from shared.my_types import Experiment, Observation, UploadInfoRequest
from shared.utils.convert.message_to_upload_request import combine_upload_info_requests


RANDOM_OBSERVATIONS_AMOUNT = 3


class ExperimentService(ApiService):
    async def get_random_observations(self, tg_user_id: int) -> list[Observation]:
        url = f'{self.base_url}/observations/random'
        params: Params = {'amount': RANDOM_OBSERVATIONS_AMOUNT}
        headers = self.get_auth_headers(tg_user_id)
        observations: RandomObservationsResponse = await self.get(url, headers=headers, params=params, dataclass=RandomObservationsResponse)

        return observations.observations

    async def get_user_current_experiment(self, tg_user_id: int) -> Experiment | None:
        url = f'{self.base_url}/experiments'
        headers = self.get_auth_headers(tg_user_id)
        experiment: Experiment | None = await self.get(url, headers=headers, dataclass=Experiment)
        return experiment

    async def run_experiment(self, tg_user_id: int, bot: Bot) -> tuple[list[Observation], Experiment]:
        observations = await self.get_random_observations(tg_user_id)
        if (len(observations) < RANDOM_OBSERVATIONS_AMOUNT):
            pass
            # TODO uncomment when test is over
            # raise NotEnoughObservationsException

        await self.mark_observations_as_seen(tg_user_id=tg_user_id, observations_ids=[o.id for o in observations])

        url = f'{self.base_url}/experiments'
        headers = self.get_auth_headers(tg_user_id)
        payload: Payload = {'observations_ids': [o.id for o in observations]}
        try:
            experiment: Experiment = await self.put(url, headers=headers, payload=payload, dataclass=Experiment)
            return observations, experiment

        except ClientResponseError as e:
            if e.code == 423:
                raise AlreadyStartedExperiment
            raise ClientResponseError

    async def complete_experiment(self, tg_user_id: int, requests: list[UploadInfoRequest]):
        url = f'{self.base_url}/experiments'
        headers = self.get_auth_headers(tg_user_id)
        request: UploadInfoRequest = combine_upload_info_requests(
            requests=requests)

        self.__validate_complete_experiment_request(request)

        payload = request.model_dump()
        try:
            await self.patch(url, headers=headers, payload=payload)
        except ClientResponseError as e:
            if e.code == 423:
                raise NotStartedExperimentException
            raise e

    async def cancel_experiment(self, tg_user_id: int):
        url = f'{self.base_url}/experiments'
        headers = self.get_auth_headers(tg_user_id)
        await self.delete(url, headers=headers)

    async def mark_observations_as_seen(self, tg_user_id: int, observations_ids: list[int]):
        url = f'{self.base_url}/observations/views'
        headers = self.get_auth_headers(tg_user_id)
        request: Payload = {'observations_ids': observations_ids}
        await self.put(url, headers=headers, payload=request)

    def __validate_complete_experiment_request(self, request: UploadInfoRequest):
        if not request.text:
            raise NoTextInExperimentResultException


experiment_service = ExperimentService()
