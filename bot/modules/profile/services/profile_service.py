from core.api_services.profile_api_service import profile_api_service


class ProfileService:
    async def get_user(tg_user_id: int):
        user = await profile_api_service.get_profile(tg_user_id)
        return user

    async def get_user_observations(tg_user_id: int, cursor: str | None = None):
        result = await profile_api_service.get_observations(tg_user_id, cursor)
        return result

    async def get_user_experiments(tg_user_id: int, cursor: str | None = None):
        result = await profile_api_service.get_user_experiments(tg_user_id, cursor)
        return result


profile_service = ProfileService()
