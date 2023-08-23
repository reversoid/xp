from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from typing import Callable

scheduler = AsyncIOScheduler()
scheduler.start()


def schedule_task(task_id: str, callback: Callable, date: datetime):
    return scheduler.add_job(
        func=callback,
        id=task_id,
        trigger='date',
        replace_existing=True,
        next_run_time=date
    )


def cancel_scheduled_task(task_id: str):
    scheduler.remove_job(task_id)
