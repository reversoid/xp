from shared.api_service import ApiService, Payload


class ProfileService(ApiService):
    async def follow_user_by_id(self, tg_user_id: int, followee_user_id: int):
        url = f'{self.base_url}/profile/followees'
        headers = self.get_auth_headers(tg_user_id=tg_user_id)
        payload: Payload = {'user_id': followee_user_id}

        await self.put(
            url, headers=headers, payload=payload)

    async def unfollow_user_by_id(self, tg_user_id: int, followee_user_id: int):
        url = f'{self.base_url}/profile/{followee_user_id}/followers'
        headers = self.get_auth_headers(tg_user_id=tg_user_id)

        await self.delete(
            url, headers=headers)

    async def follow_user_by_username(self, tg_user_id: int, username: str):
        url = f'{self.base_url}/profile/{username}/followers'
        headers = self.get_auth_headers(tg_user_id=tg_user_id)

        await self.put(
            url, headers=headers)


profile_service = ProfileService()
