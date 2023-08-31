from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData


class FollowUserCallback(CallbackData, prefix='my-followee-follow'):
    user_id: int


def get_follow_keyboard(user_id: int):
    _follow_button = InlineKeyboardButton(
        text='Follow', callback_data=FollowUserCallback(user_id=user_id).pack())

    follow_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[_follow_button]])

    return follow_keyboard
