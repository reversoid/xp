from shared.api_service import ApiService
from .dto import CreateObservationDto
from .responses import GetRandomObservationsResponse


class ObservationApiService(ApiService):
    async def create_observation(self, tg_user_id: int, dto: CreateObservationDto):
        url = self.get_url("observations")
        headers = self.get_auth_headers(tg_user_id)

        await self.post(url, payload=dto.model_dump(), headers=headers)

    async def get_random_observations(self, tg_user_id: int):
        url = self.get_url("observations/random")
        headers = self.get_auth_headers(tg_user_id)

        response: GetRandomObservationsResponse = await self.get(
            url, headers=headers, dataclass=GetRandomObservationsResponse
        )

        return response

    async def mark_observation_as_viewed(self, tg_user_id: int, observation_id: str):
        url = self.get_url(f"observations/{observation_id}/views")
        headers = self.get_auth_headers(tg_user_id)

        await self.put(url, headers=headers)


observation_api_service = ObservationApiService()
