from typing import Literal
from .responses import (
    GetSubscriptionStatusResponse,
)
from core.api_services.utils.api_service import ApiService


class SubscriptionApiService(ApiService):
    async def get_subscription_status(
        self, tg_user_id: int
    ) -> Literal["ACTIVE", "EXPIRED", "NO_SUBSCRIPTION"]:
        url = self.get_url("subscription/status")

        headers = self.get_auth_headers(tg_user_id=tg_user_id)

        response: GetSubscriptionStatusResponse = await self.get(
            url=url, headers=headers, dataclass=GetSubscriptionStatusResponse
        )

        return response.status


subscription_api_service = SubscriptionApiService()
