from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime


scheduler = BackgroundScheduler()
scheduler.start()


def schedule_task(task_id: str, callback: function, date: datetime):
    scheduler.add_job(
        callback,
        'date',
        run_date=date,
        id=task_id,
        replace_existing=True
    )


def cancel_scheduled_task(task_id: str):
    scheduler.remove_job(task_id)
