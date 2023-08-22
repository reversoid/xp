from aiogram import Router
from modules.observation.handlers.log_observation import router as _log_router


observation_router = Router()

observation_router.include_routers(
    _log_router,
)
