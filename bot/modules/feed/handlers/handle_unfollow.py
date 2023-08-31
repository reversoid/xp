from aiogram import Router
from aiogram.types import CallbackQuery
from modules.feed.keyboards.follow_keyboard import get_follow_keyboard
from modules.feed.keyboards.unfollow_keyboard import UnfollowUserCallback, get_unfollow_keyboard
from modules.profile.services import profile_service

handle_unfollow_router = Router()


@handle_unfollow_router.callback_query(UnfollowUserCallback.filter())
async def handle_unfollow_user(query: CallbackQuery):
    parsed_data = UnfollowUserCallback.unpack(query.data)

    followee_id = parsed_data.user_id

    await profile_service.unfollow_user_by_id(
        tg_user_id=query.from_user.id, followee_user_id=followee_id)

    follow_keyboard = get_follow_keyboard(followee_id)
    await query.message.edit_reply_markup(reply_markup=follow_keyboard)

    await query.answer()
