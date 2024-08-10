from aiogram import Router
from .profile import profile_router as _profile_router
from .show_my_experiments import experiments_router as _experiments_router
from .show_my_observations import observations_router as _observations_router

profile_router = Router()

profile_router.include_routers(
    _profile_router, _experiments_router, _observations_router
)
