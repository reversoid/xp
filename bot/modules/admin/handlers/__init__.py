from aiogram import BaseMiddleware, Router
from config.config import load_config
from modules.admin.handlers.handle_start_command import router as _start_router
from modules.admin.handlers.handle_subscription import (
    router as _subscription_router,
)
from modules.admin.handlers.handle_waitlist import router as _waitlist_router
from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery

config = load_config()


class AdminMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        is_message_from_admin = event.from_user.id == config.admin_bot.admin_user_id

        is_query_from_user = event.from_user.id == config.admin_bot.admin_user_id

        if not is_message_from_admin or not is_query_from_user:
            return

        return await handler(event, data)


admin_router = Router()

admin_router.message.middleware.register(AdminMiddleware())
admin_router.callback_query.middleware.register(AdminMiddleware())


admin_router.include_routers(_start_router, _subscription_router, _waitlist_router)
