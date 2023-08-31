from typing import Awaitable, Callable, Any
from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import Message
from modules.core.middlewares.SchedulerMiddleware import CoreScheduler
from .ExperimentScheduler import ExperimentScheduler


class SchedulerNotProvidedException(Exception):
    pass


class ExperiementSchedulerMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()

    async def __call__(
        self,
        handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: dict[str, Any]
    ) -> Any:
        core_scheduler = data.get('scheduler')
        if not core_scheduler or not isinstance(core_scheduler, CoreScheduler):
            raise SchedulerNotProvidedException

        data['experiment_scheduler'] = ExperimentScheduler(
            scheduler=core_scheduler)

        return await handler(event, data)
