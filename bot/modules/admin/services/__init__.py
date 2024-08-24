from datetime import datetime, timedelta, timezone

from core.api_services.observation_api_service import observation_api_service
from core.api_services.subscription_api_service import subscription_api_service
from modules.observation.services import observation_service


class AdminService:
    async def upsert_subscription(self, tg_user_id: int, username: str, days: int):
        until = datetime.now(timezone.utc) + timedelta(days=days)
        subscription = await subscription_api_service.upsert_subscription(
            tg_user_id=tg_user_id, username=username, until=until
        )
        return subscription

    async def get_waiting_observations(self, tg_user_id: int, cursor: str = None):
        return await observation_api_service.get_waitlist_observations(
            tg_user_id, cursor
        )

    async def approve_observation(self, tg_user_id: int, observation_id: str):
        await observation_api_service.approve_observation(tg_user_id, observation_id)

    async def delete_observation(self, tg_user_id: int, observation_id: str):
        await observation_api_service.delete_observation(tg_user_id, observation_id)

    async def get_waitlist_amount(
        self,
        tg_user_id: int,
    ):
        return await observation_api_service.get_waitlist_amount(tg_user_id)


admin_service = AdminService()
