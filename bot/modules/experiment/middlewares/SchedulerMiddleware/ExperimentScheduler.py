from datetime import datetime
from aiogram import Bot
from modules.core.middlewares.SchedulerMiddleware import CoreScheduler
from modules.experiment.lexicon import LEXICON

def get_experiment_task_id(tg_user_id: int):
    return f'experiment_expired_{tg_user_id}'


class ExperimentScheduler:
    def __init__(self, scheduler: CoreScheduler):
        self._scheduler = scheduler

    def schedule_send_experiment_expired(self, bot: Bot, tg_user_id: int, date: datetime):
        async def callback():
            await bot.send_message(chat_id=tg_user_id, text=LEXICON['experiment_expired'])

        return self._scheduler.schedule_task(
            callback=callback,
            date=date,
            task_id=get_experiment_task_id(tg_user_id)
        )

    def cancel_send_experiment_expired(self, tg_user_id: int):
        self._scheduler.cancel_scheduled_task(
            get_experiment_task_id(tg_user_id))
