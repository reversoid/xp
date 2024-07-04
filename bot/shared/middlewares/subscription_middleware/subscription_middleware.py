from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from modules.subcription.services import subscription_service
from .exceptions import ExpiredSubscriptionException, NoSubscriptionException
from aiogram.fsm.context import FSMContext


class SubscriptionMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        pass

    async def __call__(
        self,
        handler: Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]],
        event: Message | CallbackQuery,
        data: Dict[str, Any],
    ) -> Any:
        tg_user_id = event.from_user.id
        subscription_status = await subscription_service.get_subscription_status(
            tg_user_id
        )

        state: FSMContext = data.get("state")

        if subscription_status == "ACTIVE":
            return await handler(event, data)
        if subscription_status == "EXPIRED":
            await state.clear()
            raise ExpiredSubscriptionException
        if subscription_status == "NO_SUBSCRIPTION":
            await state.clear()
            raise NoSubscriptionException
