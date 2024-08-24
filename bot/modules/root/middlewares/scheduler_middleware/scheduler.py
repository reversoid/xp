from datetime import datetime
from typing import Callable
from apscheduler.schedulers.asyncio import AsyncIOScheduler


class CoreScheduler:
    def __init__(self, scheduler: AsyncIOScheduler):
        self._scheduler = scheduler

    def run_periodic_task(self, task_id: str, callback: Callable):
        return self._scheduler.add_job(
            func=callback,
            id=task_id,
            trigger="interval",
            replace_existing=True,
            minutes=1,
        )

    def schedule_task(self, task_id: str, callback: Callable, date: datetime):
        return self._scheduler.add_job(
            func=callback,
            id=task_id,
            trigger="date",
            replace_existing=True,
            next_run_time=date,
        )

    def cancel_scheduled_task(self, task_id: str):
        try:
            self._scheduler.remove_job(task_id)
        except:
            pass
