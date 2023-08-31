from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, CallbackQuery
from modules.profile.keyboards.follow_keyboard import FollowUserCallback, get_follow_keyboard
from modules.profile.keyboards.unfollow_keyboard import UnfollowUserCallback, get_unfollow_keyboard
from modules.profile.keyboards.next_followees_keyboard import next_followees_keyboard
from modules.profile.lexicon import LEXICON, BUTTON_LEXICON
from aiogram.fsm.context import FSMContext
from modules.profile.services import profile_service
from modules.profile.states import FSMProfile

followees_router = Router()


@followees_router.message(Command('followees'))
@followees_router.message(StateFilter(FSMProfile.viewing_followees), F.text == BUTTON_LEXICON['load_more_followees'])
async def show_followees(message: Message, state: FSMContext):
    data = await state.get_data()
    lower_bound = data.get(
        'lower_bound', None) if message.text == BUTTON_LEXICON['load_more_followees'] else None

    profiles = await profile_service.get_followees(message.from_user.id, lower_bound)

    if (len(profiles.items) == 0):
        await message.answer(text=LEXICON['empty_followees'])
        return

    await message.answer(text=LEXICON['your_followees'])

    for profile in profiles.items:
        keyboard = get_unfollow_keyboard(profile.id)
        await message.answer(text=f'{profile.username}', reply_markup=keyboard)

    if not profiles.next_key:
        await message.answer(text=LEXICON['no_more_followees'], reply_markup=None)
        return
    else:
        await state.set_state(FSMProfile.viewing_followees)
        await state.update_data(lower_bound=profiles.next_key)
        await message.answer(reply_markup=next_followees_keyboard)


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
