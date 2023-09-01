from aiogram import Router, Bot
from .get_feed import feed_router as _feed_router
from .handle_follow import handle_follow_router as _handle_follow_router
from .handle_unfollow import handle_unfollow_router as _handle_unfollow_router
from .get_followees_experiments import followees_router as _followees_router
from .get_random_experiments import random_router as _random_router

feed_router = Router()

feed_router.include_routers(
    _feed_router, _handle_follow_router, _handle_unfollow_router, _followees_router, _random_router)
