from core.api_services.profile_api_service import profile_api_service
from core.models import User
from modules.profile.services.exceptions import AlreadyTakenTrialException
from core.api_services.subscription_api_service.exceptions import (
    TrialAlreadyTakenException,
)


class ProfileService:
    async def get_user(self, tg_user_id: int) -> User | None:
        user = await profile_api_service.get_profile(tg_user_id)
        return user

    async def get_subscription_status(self, tg_user_id: int):
        status = await profile_api_service.get_subscription_status(tg_user_id)
        return status

    async def get_trial_subscription(self, tg_user_id: int):
        try:
            subscription = await profile_api_service.start_trial(tg_user_id)
            return subscription
        except TrialAlreadyTakenException:
            raise AlreadyTakenTrialException

    async def get_user_observations(self, tg_user_id: int, cursor: str | None = None):
        result = await profile_api_service.get_observations(tg_user_id, cursor)
        return result

    async def get_user_experiments(self, tg_user_id: int, cursor: str | None = None):
        result = await profile_api_service.get_user_experiments(tg_user_id, cursor)
        return result


profile_service = ProfileService()
