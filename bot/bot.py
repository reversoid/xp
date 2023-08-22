import asyncio
import logging
from aiogram.fsm.storage.redis import RedisStorage, Redis
from aiogram import Bot, Dispatcher
from config_data.config import load_config

from modules.core.handlers import core_router
from modules.core.utils import set_main_menu
from modules.experiment.handlers import experiment_router
from modules.feed.handlers import feed_router
from modules.observation.handlers import observation_router
from modules.profile.handlers import profile_router

logger = logging.getLogger(__name__)


async def main():
    config = load_config()
    bot = Bot(token=config.bot.token)

    redis = Redis(host=config.database.redis.host,
                  password=config.database.redis.password, port=config.database.redis.port)

    storage = RedisStorage(redis=redis)

    dp = Dispatcher(storage=storage)

    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    dp.include_routers(
        experiment_router,
        feed_router,
        observation_router,
        profile_router,
        core_router,
    )

    await set_main_menu(bot)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if (__name__ == '__main__'):
    asyncio.run(main())
