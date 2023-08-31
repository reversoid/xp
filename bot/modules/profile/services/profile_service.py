from .responses import PaginatedUsersResponse
from shared.api_service import ApiException, ApiService, Payload, Params


class AlreadySubscribedException(Exception):
    pass


class NoSuchUserException(Exception):
    pass


class ProfileService(ApiService):
    async def follow_user_by_id(self, tg_user_id: int, followee_user_id: int):
        url = f'{self.base_url}/profile/followees'
        headers = self.get_auth_headers(tg_user_id=tg_user_id)
        payload: Payload = {'user_id': followee_user_id}

        await self.put(
            url, headers=headers, payload=payload)

    async def get_followees(self, tg_user_id: int, lower_bound: str | None = None) -> PaginatedUsersResponse:
        limit = 1
        url = f'{self.base_url}/profile/followees'
        headers = self.get_auth_headers(tg_user_id=tg_user_id)
        params: Params = {'limit': limit}

        if lower_bound:
            params['lower_bound'] = lower_bound

        profiles = await self.get(
            url, headers=headers, params=params, dataclass=PaginatedUsersResponse)
        return profiles

    async def unfollow_user_by_id(self, tg_user_id: int, followee_user_id: int):
        url = f'{self.base_url}/profile/{followee_user_id}/followers'
        headers = self.get_auth_headers(tg_user_id=tg_user_id)

        await self.delete(
            url, headers=headers)

    async def follow_user_by_username(self, tg_user_id: int, username: str):
        url = f'{self.base_url}/profile/{username}/followers'
        headers = self.get_auth_headers(tg_user_id=tg_user_id)

        try:
            await self.put(
                url, headers=headers)
        except ApiException as e:
            if (e.message == 'ALREADY_SUBSCRIBED'):
                raise AlreadySubscribedException
            if (e.message == 'NO_SUCH_USER'):
                raise NoSuchUserException
            raise e


profile_service = ProfileService()
