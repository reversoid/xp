from datetime import datetime
from typing import Literal

from core.models.subscription import Subscription
from .responses import (
    GetSubscriptionStatusResponse,
    UpsertSubscriptionResponse,
)
from core.api_services.utils.api_service import ApiService, Payload


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

    async def upsert_subscription(
        self, tg_user_id: int, username: str, until: datetime
    ):
        url = self.get_url("admin/subscriptions")

        headers = self.get_auth_headers(tg_user_id=tg_user_id)

        payload: Payload = {
            "username": username,
            "until": until.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z",
        }

        response: UpsertSubscriptionResponse = await self.put(
            url=url,
            headers=headers,
            dataclass=UpsertSubscriptionResponse,
            payload=payload,
        )

        return response.subscription


subscription_api_service = SubscriptionApiService()
