from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from modules.experiment.utils.send_experiments import send_experiments
from modules.feed.keyboards.follow_keyboard import FollowUserCallback
from modules.feed.lexicon import LEXICON
from modules.feed.services import feed_service
from modules.feed.services.responses.feed_response import FeedResponse

from modules.feed.states import FSMFeed

handle_follow_router = Router()


@handle_follow_router.callback_query(FollowUserCallback.filter())
async def handle_follow_user(message: Message, bot: Bot, query: FollowUserCallback):
    # TODO follow user
    pass
