from typing import Awaitable, Callable, Any
from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import Message
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from .scheduler import CoreScheduler


class SchedulerMiddleware(BaseMiddleware):
    def __init__(self, scheduler: AsyncIOScheduler):
        super().__init__()
        self._scheduler = CoreScheduler(scheduler)

    async def __call__(
        self,
        handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: dict[str, Any],
    ) -> Any:
        data["scheduler"] = self._scheduler
        return await handler(event, data)
