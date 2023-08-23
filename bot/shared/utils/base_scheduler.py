from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from typing import Callable
scheduler = AsyncIOScheduler()
scheduler.start()


def schedule_task(task_id: str, callback: Callable, date: datetime):
    scheduler.add_job(
        callback,
        'date',
        run_date=date,
        id=task_id,
        replace_existing=True
    )


def cancel_scheduled_task(task_id: str):
    scheduler.remove_job(task_id)
