from aiogram import Router, F, Bot
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from modules.profile.keyboards.follow_keyboard import FollowUserCallback, get_follow_keyboard
from modules.profile.keyboards.profile_keyboard import ProfileFolloweesCallback
from modules.profile.keyboards.unfollow_keyboard import UnfollowUserCallback, get_unfollow_keyboard
from modules.profile.keyboards.next_followees_keyboard import next_followees_keyboard
from modules.profile.lexicon import LEXICON, BUTTON_LEXICON
from aiogram.fsm.context import FSMContext
from modules.profile.services import profile_service
from modules.profile.states import FSMProfile
from shared.lexicon import SHARED_LEXICON

followees_router = Router()


@followees_router.callback_query(ProfileFolloweesCallback.filter())
@followees_router.message(StateFilter(FSMProfile.viewing_followees), F.text == BUTTON_LEXICON['load_more_followees'])
async def show_followees(message: Message | CallbackQuery, state: FSMContext, bot: Bot, query: CallbackQuery | None = None):
    data = await state.get_data()
    lower_bound = data.get(
        'lower_bound', None) if isinstance(message, Message) and message.text == BUTTON_LEXICON['load_more_followees'] else None

    user_id = query.from_user.id if query else message.from_user.id

    profiles = await profile_service.get_followees(user_id, lower_bound)

    if (len(profiles.items) == 0):
        await bot.send_message(chat_id=user_id, text=LEXICON['empty_followees'])
        return

    await bot.send_message(chat_id=user_id, text=LEXICON['your_followees']) if not lower_bound else None

    for profile in profiles.items:
        keyboard = get_unfollow_keyboard(profile.id)
        await bot.send_message(chat_id=user_id, text=f'{profile.username}', reply_markup=keyboard)

    if not profiles.next_key:
        await state.clear()
        await bot.send_message(chat_id=user_id, text=LEXICON['no_more_followees'], reply_markup=ReplyKeyboardRemove())
        return
    else:
        await state.set_state(FSMProfile.viewing_followees)
        await state.update_data(lower_bound=profiles.next_key)
        await bot.send_message(chat_id=user_id, text=LEXICON['exists_more_followees'], reply_markup=next_followees_keyboard)


@followees_router.callback_query(UnfollowUserCallback.filter())
async def unfollow(query: CallbackQuery):
    parsed_data = UnfollowUserCallback.unpack(query.data)

    followee_id = parsed_data.user_id

    await profile_service.unfollow_user_by_id(
        tg_user_id=query.from_user.id, followee_user_id=followee_id)

    follow_keyboard = get_follow_keyboard(followee_id)
    await query.message.edit_reply_markup(reply_markup=follow_keyboard)


@followees_router.callback_query(FollowUserCallback.filter())
async def follow(query: CallbackQuery):
    parsed_data = FollowUserCallback.unpack(query.data)

    followee_id = parsed_data.user_id

    await profile_service.follow_user_by_id(
        tg_user_id=query.from_user.id, followee_user_id=followee_id)

    follow_keyboard = get_unfollow_keyboard(followee_id)
    await query.message.edit_reply_markup(reply_markup=follow_keyboard)


@followees_router.message(StateFilter(FSMProfile.viewing_followees), F.text == BUTTON_LEXICON['cancel_showing_followees'])
async def cancel_show_experiments(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(text=SHARED_LEXICON['ok'], reply_markup=ReplyKeyboardRemove())
