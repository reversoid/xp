from aiogram import Router, Bot, F
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from modules.experiment.utils.send_experiments import send_experiments
from modules.feed.lexicon import BUTTON_LEXICON, LEXICON
from modules.feed.services.feed_service import ExceededRandomExperiments, feed_service
from modules.feed.keyboards.next_feed_keyboard import next_feed_keyboard
from modules.feed.keyboards.feed_keyboard import FeedRandomCallback

from modules.feed.states import FSMFeed

random_router = Router()


@random_router.callback_query(FeedRandomCallback.filter())
@random_router.message(StateFilter(FSMFeed.reading_random), F.text == BUTTON_LEXICON['load_more_experiments'])
async def handle_get_random(query: CallbackQuery, state: FSMContext, bot: Bot, message: Message | None = None):
    user_id = query.from_user.id if query else message.from_user.id
    message_to_answer = query.message if query else message
    if not message_to_answer:
        return

    try:
        random_experiments = await feed_service.get_random_unseen_experiments(user_id, limit=5)

        if len(random_experiments.items) == 0:
            await message_to_answer.answer(text=LEXICON['no_random_experiments'])
            return

        await message_to_answer.answer(text=LEXICON['showing_random'])

        await send_experiments(bot=bot, experiments=random_experiments.items, tg_user_id=user_id)

        if (random_experiments.next_key):
            await state.set_state(FSMFeed.reading_random)
            await message_to_answer.answer(text=LEXICON['has_more_feed'], reply_markup=next_feed_keyboard)
        else:
            await state.clear()
            await message_to_answer.answer(text=LEXICON['no_more_feed'], reply_markup=ReplyKeyboardRemove())

    except ExceededRandomExperiments:
        await message_to_answer.answer(text=LEXICON['exceeded_random_experiments'])
