class ExperimentService:
    async def run_experiment(
        self, tg_user_id: int, bot: Bot
    ) -> tuple[list[Observation], Experiment]:
        observations = await self.get_random_observations(tg_user_id)
        # if (len(observations) < RANDOM_OBSERVATIONS_AMOUNT):
        #     raise NotEnoughObservationsException

        await self.mark_observations_as_seen(
            tg_user_id=tg_user_id, observations_ids=[o.id for o in observations]
        )

        url = f"{self.base_url}/experiments"
        headers = self.get_auth_headers(tg_user_id)
        payload: Payload = {"observations_ids": [o.id for o in observations]}
        try:
            experiment: Experiment = await self.put(
                url, headers=headers, payload=payload, dataclass=Experiment
            )
            return observations, experiment

        except ApiException as e:
            if e.message == "EXPERIMENT_ALREADY_STARTED":
                raise AlreadyStartedExperiment
            raise e

    async def complete_experiment(
        self, tg_user_id: int, requests: list[UploadInfoRequest]
    ):
        url = f"{self.base_url}/experiments"
        headers = self.get_auth_headers(tg_user_id)
        request: UploadInfoRequest = combine_upload_info_requests(requests=requests)

        print(request)

        self.__validate_complete_experiment_request(request)

        payload = request.model_dump()
        try:
            await self.patch(url, headers=headers, payload=payload)
        except ApiException as e:
            if e.message == "EXPERIMENT_NOT_STARTED":
                raise NotStartedExperimentException
            raise e

    async def cancel_experiment(self, tg_user_id: int):
        url = f"{self.base_url}/experiments"
        headers = self.get_auth_headers(tg_user_id)
        await self.delete(url, headers=headers)

    async def mark_observations_as_seen(
        self, tg_user_id: int, observations_ids: list[str]
    ):
        url = f"{self.base_url}/observations/views"
        headers = self.get_auth_headers(tg_user_id)
        request: Payload = {"observations_ids": observations_ids}
        await self.put(url, headers=headers, payload=request)

    def __validate_complete_experiment_request(self, request: UploadInfoRequest):
        if not request.text:
            raise NoTextInExperimentResultException
