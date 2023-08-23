from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters.callback_data import CallbackData

from modules.experiment.lexicon import BUTTON_LEXICON


_cancel_button = KeyboardButton(text=BUTTON_LEXICON['cancel'])
_finish_button = KeyboardButton(text=BUTTON_LEXICON['finish'])


started_experiment_keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True, is_persistent=True, keyboard=[[_cancel_button, _finish_button]], selective=True)
