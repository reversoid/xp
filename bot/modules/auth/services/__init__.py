from shared.api_service import ApiService, Headers, Params, Payload
import string
import secrets
from pydantic import BaseModel


class CheckUserRegistrationResponse(BaseModel):
    registered: bool
    username: str | None = None


def generate_password(length=16):
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password


class AuthService(ApiService):
    async def is_user_registered(self, tg_user_id: int) -> CheckUserRegistrationResponse:
        url = f'{self.base_url}/auth/is_registered_tg'
        headers: Headers = self.get_auth_headers()
        params: Params = {'tg_user_id': tg_user_id}
        response: CheckUserRegistrationResponse = await self.get(url, dataclass=CheckUserRegistrationResponse, headers=headers, params=params)
        return response

    async def register(self, tg_user_id: int, username: str):
        url = f'{self.base_url}/auth/register'
        random_password = generate_password(16)
        payload: Payload = {'username': username,
                            'password': random_password, 'tg_user_id': tg_user_id}

        await self.post(url, payload=payload)


auth_service = AuthService()
