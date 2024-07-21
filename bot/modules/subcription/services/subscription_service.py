from typing import Literal
from core.api_services.subscription_api_service import (
    subscription_api_service,
)


# TODO can somehow use name convetion of api exceptions and service exceptions?


class SubscriptionService:
    async def get_subscription_status(
        self, tg_user_id: int
    ) -> Literal["ACTIVE", "EXPIRED", "NO_SUBSCRIPTION"]:
        status = await subscription_api_service.get_subscription_status(tg_user_id)
        return status


subscription_service = SubscriptionService()
