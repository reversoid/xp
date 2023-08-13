import asyncio
import logging
from aiogram import Bot, Dispatcher
from keyboards.main_menu import set_main_menu
from config_data.config import load_config, Config
from handlers import routers

logger = logging.getLogger(__name__)

async def main():
    config = load_config()

    bot = Bot(token=config.bot.token)
    dp = Dispatcher()

    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    dp.include_routers(*routers)

    await set_main_menu(bot)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if (__name__ == '__main__'):
    asyncio.run(main())
