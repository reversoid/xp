from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData


class UnfollowUserCallback(CallbackData, prefix='my-followee-unfollow'):
    user_id: int


def get_unfollow_keyboard(user_id: int):
    _unfollow_button = InlineKeyboardButton(
        text='Unfollow', callback_data=UnfollowUserCallback(user_id=user_id).pack())

    unfollow_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[_unfollow_button]])

    return unfollow_keyboard
