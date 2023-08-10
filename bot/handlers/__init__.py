from .other_handlers import router as other_router
from .user_handlers import router as user_router

routers = [user_router, other_router]

__all__ = ['routers']
