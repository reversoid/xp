from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from modules.profile.lexicon import BUTTON_LEXICON


_cancel_button = KeyboardButton(
    text=BUTTON_LEXICON['cancel_showing_followees'])
_load_more_button = KeyboardButton(text=BUTTON_LEXICON['load_more_followees'])


next_followees_keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True, is_persistent=True, keyboard=[[_cancel_button, _load_more_button]], selective=True)
