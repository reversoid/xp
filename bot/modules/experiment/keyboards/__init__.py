from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData


class StartExperimentCallback(CallbackData, prefix='experiment'):
    pass


_confirm_start_experiment_button = InlineKeyboardButton(
    text='Absolutely', callback_data=StartExperimentCallback().pack())

confirm_start_experiment_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[_confirm_start_experiment_button]])