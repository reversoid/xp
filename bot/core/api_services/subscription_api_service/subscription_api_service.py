from typing import Literal

from core.api_services.subscription_api_service.exceptions import (
    TrialAlreadyTakenException,
)
from core.models.subscription import Subscription
from .responses import (
    GetSubscriptionStatusResponse,
    GetTriaResponse,
)
from core.api_services.utils.api_service import ApiException, ApiService, Params


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

    async def start_trial(self, tg_user_id: int) -> Subscription:
        url = self.get_url("subscription/trial")

        headers = self.get_auth_headers(tg_user_id=tg_user_id)

        try:
            response: GetTriaResponse = await self.put(
                url=url, headers=headers, dataclass=GetTriaResponse, payload={}
            )
            return response.subscription
        except ApiException as e:
            if e.message == "TRIAL_ALREADY_TAKEN":
                raise TrialAlreadyTakenException
            raise e


subscription_api_service = SubscriptionApiService()
