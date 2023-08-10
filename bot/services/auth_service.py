from dataclasses import dataclass
from typing import Any, cast
import aiohttp
from .api_service import ApiService


@dataclass
class CheckUserRegistrationResponse:
    registered: bool


class AuthService(ApiService):
    async def check_user_registration(self, tg_user_id: int):
        url = f'/is_registered_tg'
        registered: bool = (await self.get(url, CheckUserRegistrationResponse)).registered
        return registered

    async def register(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.post(url) as response:
                return await response.text()
