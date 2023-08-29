from modules.feed.services.responses.feed_response import FeedResponse
from shared.api_service import ApiService, Params, Payload


class FeedService(ApiService):
    async def get_followee_experiments(self, tg_user_id: int) -> FeedResponse:
        limit = 5
        url = f'{self.base_url}/feed/experiments/followee'
        params: Params = {'limit': limit}
        headers = self.get_auth_headers(tg_user_id=tg_user_id)
        followee_experiments: FeedResponse = await self.get(
            url, params=params, dataclass=FeedResponse, headers=headers)

        await self.mark_experiments_as_seen(tg_user_id=tg_user_id, experiments_ids=[
            item.id for item in followee_experiments.items])

        return followee_experiments

    async def get_random_unseen_experiments(self, tg_user_id: int, limit: int) -> FeedResponse:
        limit = 5
        url = f'{self.base_url}/feed/experiments/random'
        params: Params = {'limit': limit}
        headers = self.get_auth_headers(tg_user_id=tg_user_id)
        random_experiments: FeedResponse = await self.get(
            url, params=params, dataclass=FeedResponse, headers=headers)

        await self.mark_experiments_as_seen(tg_user_id=tg_user_id, experiments_ids=[
            item.id for item in random_experiments.items])

        return random_experiments

    async def mark_experiments_as_seen(self, tg_user_id: int, experiments_ids: list[int]):
        url = f'{self.base_url}/feed/experiments/views'
        headers = self.get_auth_headers(tg_user_id)
        request: Payload = {'experiments_ids': experiments_ids}
        await self.put(url, headers=headers, payload=request)


feed_service = FeedService()
