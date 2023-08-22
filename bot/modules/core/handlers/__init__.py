from .other import other_router as _other_router
from .handle_start_command import start_router as _start_router
from .help import help_router
from aiogram import Router

core_router = Router()

core_router.include_routers(_start_router, help_router, _other_router)
