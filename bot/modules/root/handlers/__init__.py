from .handle_start_command import start_router as _start_router
from .help import help_router
from aiogram import Router
from .other import other_router
from .error import error_router
from .handle_buy_subscription import buy_subscription_router
from .handle_learn_more_subscription import learn_more_subscription_router

core_router = Router()

core_router.include_routers(
    _start_router, help_router, buy_subscription_router, learn_more_subscription_router
)
