from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from modules.feed.lexicon import LEXICON
from modules.feed.services import feed_service
from modules.feed.services.responses.feed_response import FeedResponse

from modules.feed.states import FSMFeed

feed_router = Router()


@feed_router.message(Command('feed'))
async def handle_feed_command(message: Message, state: FSMContext):
    await state.set_state(FSMFeed.reading_followee)

    followee_experiments = await feed_service.get_followee_experiments(
        message.from_user.id)

    followee_experiments_exist = len(followee_experiments.items) != 0

    if followee_experiments_exist:
        # TODO send experiments
        pass
        return

    await message.answer(text=LEXICON['no_followee_experiments'])
    await message.answer(text=LEXICON['showing_random'])

    random_experiments: FeedResponse = await feed_service.get_random_unseen_experiments(
        message.from_user.id)

    random_experiments_exist = len(random_experiments.items) != 0

    if random_experiments_exist:
        # TODO send experiments
        pass
    else:
        await message.answer(text=LEXICON['no_random_experiments'])
