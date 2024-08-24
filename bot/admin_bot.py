import asyncio
import logging
from aiogram.fsm.storage.redis import RedisStorage, Redis
from aiogram import Bot, Dispatcher
from config import load_config
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from modules.root.middlewares.scheduler_middleware import SchedulerMiddleware
from modules.admin.handlers import admin_router

from modules.admin.utils.set_main_menu import set_main_menu
from aiogram.fsm.storage.base import DefaultKeyBuilder
from modules.root.middlewares.scheduler_middleware.scheduler import CoreScheduler
from modules.admin.services import admin_service


logger = logging.getLogger(__name__)


async def main():
    config = load_config()
    bot = Bot(token=config.bot.token)

    redis = Redis(
        host=config.database.redis.host,
        password=config.database.redis.password,
        port=config.database.redis.port,
    )

    storage = RedisStorage(
        redis=redis, key_builder=DefaultKeyBuilder(prefix="admin_fsm")
    )

    dp = Dispatcher(storage=storage)

    scheduler = AsyncIOScheduler()

    core_scheduler = CoreScheduler(scheduler)

    async def notify_about_new_observations():
        print("HELLO WORLD!")

        amount = await admin_service.get_waitlist_amount(123)
        if not amount:
            await redis.set("has_new_observations", 0)
            return

        encoded_has = await redis.get("has_new_observations")

        already_sent_notification = bool(
            int(encoded_has.decode()) if encoded_has else 0
        )

        if not already_sent_notification:
            await bot.send_message(
                config.admin_bot.admin_user_id,
                "Есть новые наблюдения",
                disable_notification=True,
            )

        await redis.set("has_new_observations", 1)

    core_scheduler.run_periodic_task(
        "new_observations_notification", notify_about_new_observations, 60
    )

    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s "
        "[%(asctime)s] - %(name)s - %(message)s",
    )

    # Выводим в консоль информацию о начале запуска бота
    logger.info("Starting bot")

    dp.include_routers(admin_router)

    await set_main_menu(bot)

    await bot.delete_webhook(drop_pending_updates=True)

    scheduler.start()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
