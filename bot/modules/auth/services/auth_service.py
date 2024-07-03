from core.api_services.auth_api_service import UserExistsException, auth_api_service
from .exceptions import UserAlreadyExistsException


class AuthService:
    async def register(self, tg_user_id: int, tg_username: str):
        try:
            await auth_api_service.register(tg_user_id, tg_username)
        except UserExistsException:
            raise UserAlreadyExistsException


auth_service = AuthService()
