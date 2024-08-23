from datetime import datetime, timedelta

from core.api_services.subscription_api_service import subscription_api_service


class AdminService:
    async def upsert_subscription(self, tg_user_id: int, username: str, days: int):
        until = datetime.now() + timedelta(days=days)
        subscription = await subscription_api_service.upsert_subscription(
            tg_user_id=tg_user_id, username=username, until=until
        )
        return subscription

    # TODO methods

    async def get_waiting_observations(tg_user_id: int):
        pass

    async def approve_observation(tg_user_id: int):
        pass

    async def remove_observation(tg_user_id: int):
        pass


admin_service = AdminService()
