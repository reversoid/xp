from core.api_services.profile_api_service.responses import PaginatedObservations
from core.api_services.utils.api_service import ApiService, Params
from .dto import CreateObservationDto
from .responses import GetRandomObservationsResponse, GetWaitlistObservationsResponse


class ObservationApiService(ApiService):
    async def create_observation(self, tg_user_id: int, dto: CreateObservationDto):
        url = self.get_url("observations")
        headers = self.get_auth_headers(tg_user_id)

        await self.post(url, payload=dto.model_dump(), headers=headers)

    async def get_waitlist_observations(
        self, tg_user_id: int, cursor: str = None
    ) -> PaginatedObservations:
        url = self.get_url("admin/observations/waitlist")
        headers = self.get_auth_headers(tg_user_id)

        params: Params = {"limit": 5}

        if cursor:
            params["cursor"] = cursor

        response: GetWaitlistObservationsResponse = await self.get(
            url,
            headers=headers,
            params=params,
            dataclass=GetWaitlistObservationsResponse,
        )

        return response.observations

    async def approve_observation(self, tg_user_id: int, observation_id: str):
        url = self.get_url(f"admin/observations/waitlist/{observation_id}")
        headers = self.get_auth_headers(tg_user_id)

        await self.patch(url, headers=headers, payload={})

    async def delete_observation(self, tg_user_id: int, observation_id: str):
        url = self.get_url(f"admin/observations/waitlist/{observation_id}")
        headers = self.get_auth_headers(tg_user_id)

        await self.delete(
            url,
            headers=headers,
        )

    async def get_random_observations(self, tg_user_id: int, limit: int):
        url = self.get_url("observations/random")
        headers = self.get_auth_headers(tg_user_id)

        response: GetRandomObservationsResponse = await self.get(
            url,
            headers=headers,
            dataclass=GetRandomObservationsResponse,
            params={"limit": str(limit)},
        )

        return response.observations

    async def mark_observation_as_viewed(self, tg_user_id: int, observation_id: str):
        url = self.get_url(f"observations/{observation_id}/views")
        headers = self.get_auth_headers(tg_user_id)

        await self.put(url, headers=headers, payload={})


observation_api_service = ObservationApiService()
