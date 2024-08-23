from aiogram import Router
from modules.admin.handlers.handle_start_command import router as _start_router
from modules.admin.handlers.handle_subscription import (
    router as _subscription_router,
)
from modules.admin.handlers.handle_waitlist import router as _waitlist_router


admin_router = Router()


admin_router.include_routers(_start_router, _subscription_router, _waitlist_router)
