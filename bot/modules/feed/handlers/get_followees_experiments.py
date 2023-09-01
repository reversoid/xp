from aiogram import Router, Bot, F
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from modules.experiment.utils.send_experiments import send_experiments
from modules.feed.lexicon import BUTTON_LEXICON, LEXICON
from modules.feed.services import feed_service
from modules.feed.keyboards.next_feed_keyboard import next_feed_keyboard
from modules.feed.keyboards.feed_keyboard import FeedFolloweesCallback

from modules.feed.states import FSMFeed

followees_router = Router()


@followees_router.callback_query(FeedFolloweesCallback.filter())
@followees_router.message(StateFilter(FSMFeed.reading_followee), F.text == BUTTON_LEXICON['load_more_experiments'])
async def handle_get_followees(query: CallbackQuery, state: FSMContext, bot: Bot, message: Message | None = None):
    data = await state.get_data()
    lower_bound = data.get(
        'lower_bound', None) if message and message.text == BUTTON_LEXICON['load_more_experiments'] else None

    user_id = query.from_user.id if query else message.from_user.id

    followee_experiments = await feed_service.get_followee_experiments(user_id, lower_bound=lower_bound)

    message_to_answer = query.message if query else message

    if not message_to_answer:
        return

    if len(followee_experiments.items) == 0:
        await message_to_answer.answer(text=LEXICON['no_followee_experiments'])
        return

    await message_to_answer.answer(text=LEXICON['followee_experiments'])

    await send_experiments(bot=bot, experiments=followee_experiments.items, tg_user_id=user_id)

    if (followee_experiments.next_key):
        await state.set_state(FSMFeed.reading_followee)
        await state.update_data(lower_bound=followee_experiments.next_key)

        await message_to_answer.answer(text=LEXICON['has_more_feed'], reply_markup=next_feed_keyboard)
    else:
        await state.clear()
        await message_to_answer.answer(text=LEXICON['no_more_feed'], reply_markup=ReplyKeyboardRemove())
