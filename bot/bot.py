import asyncio
import logging
from aiogram.fsm.storage.redis import RedisStorage, Redis
from aiogram import Bot, Dispatcher
from config import load_config
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from modules.core.middlewares.SchedulerMiddleware import SchedulerMiddleware


from modules.core.handlers import core_router, other_router
from modules.core.utils.set_main_menu import set_main_menu
from modules.experiment.handlers import experiment_router
from modules.observation.handlers import observation_router
from modules.profile.handlers import profile_router

logger = logging.getLogger(__name__)


async def main():
    config = load_config()
    bot = Bot(token=config.bot.token)

    redis = Redis(
        host=config.database.redis.host,
        password=config.database.redis.password,
        port=config.database.redis.port,
    )

    storage = RedisStorage(redis=redis)

    dp = Dispatcher(storage=storage)

    scheduler = AsyncIOScheduler()

    dp.message.middleware.register(SchedulerMiddleware(scheduler=scheduler))
    dp.callback_query.middleware.register(SchedulerMiddleware(scheduler=scheduler))

    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s "
        "[%(asctime)s] - %(name)s - %(message)s",
    )

    # Выводим в консоль информацию о начале запуска бота
    logger.info("Starting bot")

    dp.include_routers(
        core_router, experiment_router, observation_router, profile_router, other_router
    )

    await set_main_menu(bot)

    await bot.delete_webhook(drop_pending_updates=True)

    scheduler.start()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
