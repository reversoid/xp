from .handle_start_command import start_router as _start_router
from .help import help_router
from aiogram import Router
from .other import other_router
from .error import error_router
from .handle_start_trial import start_trial_router
from .handle_learn_more_trial import learn_more_trial_router

core_router = Router()

core_router.include_routers(
    _start_router, help_router, start_trial_router, learn_more_trial_router
)
