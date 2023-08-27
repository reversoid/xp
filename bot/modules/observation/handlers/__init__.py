from aiogram import Router
from modules.observation.handlers.log_observation import router as _log_router
from modules.observation.handlers.handle_log_observation import router as _handle_log_router


observation_router = Router()

observation_router.include_routers(
    _log_router,
    _handle_log_router
)
