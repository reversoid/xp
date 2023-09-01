from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData


class FeedFolloweesCallback(CallbackData, prefix='feed-followees'):
    pass


class FeedRandomCallback(CallbackData, prefix='feed-random'):
    pass


_followees_button = InlineKeyboardButton(
    text='Followees', callback_data=FeedFolloweesCallback().pack())

_random_button = InlineKeyboardButton(
    text='Random', callback_data=FeedRandomCallback().pack())


feed_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[_followees_button, _random_button]])
