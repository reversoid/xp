from typing import Literal
from core.api_services.subscription_api_service import (
    subscription_api_service,
    TrialAlreadyTakenException,
)
from core.models.subscription import Subscription
from .exceptions import AlreadyTakenTrialException

# TODO can somehow use name convetion of api exceptions and service exceptions?


class SubscriptionService:
    async def get_subscription_status(
        self, tg_user_id: int
    ) -> Literal["ACTIVE", "EXPIRED", "NO_SUBSCRIPTION"]:
        status = await subscription_api_service.get_subscription_status(tg_user_id)
        return status

    async def start_trial(self, tg_user_id: int) -> Subscription:
        try:
            subscription = await subscription_api_service.start_trial(tg_user_id)
            return subscription
        except TrialAlreadyTakenException:
            raise AlreadyTakenTrialException


subscription_service = SubscriptionService()
