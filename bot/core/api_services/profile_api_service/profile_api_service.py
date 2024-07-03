from .responses import (
    PaginatedExperimentsResponse,
    PaginatedObservationsResponse,
    ProfileResponse,
)
from core.api_services.utils.api_service import ApiService, Params
from core.models import User


class ProfileApiService(ApiService):
    async def get_profile(self, tg_user_id: int) -> User:
        url = self.get_url("profile")

        headers = self.get_auth_headers(tg_user_id=tg_user_id)

        response: ProfileResponse = await self.get(
            url=url, headers=headers, dataclass=ProfileResponse
        )
        return response.user

    async def get_user_experiments(
        self, tg_user_id: int, cursor: str | None = None
    ) -> PaginatedExperimentsResponse:
        url = self.get_url("profile/experiments")
        limit = 5

        headers = self.get_auth_headers(tg_user_id=tg_user_id)
        params: Params = {"limit": limit}
        if cursor:
            params["cursor"] = cursor

        response: PaginatedExperimentsResponse = await self.get(
            url=url,
            headers=headers,
            params=params,
            dataclass=PaginatedExperimentsResponse,
        )
        return response

    async def get_observations(
        self, tg_user_id: int, cursor: str | None = None
    ) -> PaginatedObservationsResponse:
        url = self.get_url("/profile/observations")
        limit = 5

        headers = self.get_auth_headers(tg_user_id=tg_user_id)
        params: Params = {"limit": limit}
        if cursor:
            params["cursor"] = cursor

        response: PaginatedObservationsResponse = await self.get(
            url, headers=headers, params=params, dataclass=PaginatedObservationsResponse
        )
        return response


profile_api_service = ProfileApiService()
