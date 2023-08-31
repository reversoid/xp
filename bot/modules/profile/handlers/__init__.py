from aiogram import Router
from .profile import profile_router as _profile_router
from .follow import follow_router as _follow_router
from .show_my_followee import followees_router as _followees_router
from .show_my_experiments import experiments_router as _experiments_router
from .show_my_observations import observations_router as _observations_router

profile_router = Router()

profile_router.include_routers(_profile_router, _follow_router,
                               _followees_router, _experiments_router, _observations_router)
