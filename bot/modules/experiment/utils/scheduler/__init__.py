from datetime import datetime
from aiogram import Bot
from .get_experiment_task_id import get_experiment_task_id

from shared.utils.base_scheduler import schedule_task, cancel_scheduled_task
from modules.experiment.lexicon import LEXICON


def send_experiment_expired_message(bot: Bot, tg_user_id: int, date: datetime):
    task_id = get_experiment_task_id(tg_user_id=tg_user_id)

    async def callback(): await bot.send_message(
        chat_id=tg_user_id, text=LEXICON['experiment_expired'])

    schedule_task(task_id=task_id, callback=callback, date=date)


def cancel_send_expired_message(tg_user_id: int):
    task_id = get_experiment_task_id(tg_user_id=tg_user_id)

    cancel_scheduled_task(task_id=task_id)
