from aiogram import Router
from aiogram.types import CallbackQuery
from modules.feed.keyboards.follow_keyboard import FollowUserCallback
from modules.feed.keyboards.unfollow_keyboard import get_unfollow_keyboard
from modules.profile.services import profile_service

handle_follow_router = Router()


@handle_follow_router.callback_query(FollowUserCallback.filter())
async def handle_follow_user(query: CallbackQuery):
    parsed_data = FollowUserCallback.unpack(query.data)

    followee_id = parsed_data.user_id

    await profile_service.follow_user_by_id(
        tg_user_id=query.from_user.id, followee_user_id=followee_id)

    unfollow_keyboard = get_unfollow_keyboard(followee_id)
    await query.message.edit_reply_markup(reply_markup=unfollow_keyboard)

    await query.answer()
