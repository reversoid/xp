import asyncio
from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import Message
from modules.profile.services import profile_service


class PaymentMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        pass

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        tg_user_id = event.from_user.id
        subscription_status = await profile_service.get_subscription_status(tg_user_id)
        if subscription_status == "ACTIVE":
            return await handler(event, data)
        if subscription_status == "EXPIRED":
            raise
        if subscription_status == "NO_SUBSCRIPTION":
            raise
