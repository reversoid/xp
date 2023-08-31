from aiogram import Router
from .profile import profile_router as _profile_router
from .follow import follow_router as _follow_router

profile_router = Router()

profile_router.include_routers(_profile_router, _follow_router)
