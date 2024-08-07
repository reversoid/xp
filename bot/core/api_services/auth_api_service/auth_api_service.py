from core.api_services.utils.api_service import (
    ApiException,
    ApiService,
)
from .dto import RegisterUserDto
from .exceptions import UserExistsException


class AuthApiService(ApiService):
    async def register(self, tg_user_id: int, tg_username: str):
        url = self.get_url("auth/register")

        dto = RegisterUserDto(tgId=tg_user_id, tgUsername=tg_username)

        payload = dto.model_dump()

        try:
            await self.post(url, payload=payload)
        except ApiException as e:
            if e.message == "USER_ALREADY_EXISTS":
                raise UserExistsException
            raise e


auth_api_service = AuthApiService()
