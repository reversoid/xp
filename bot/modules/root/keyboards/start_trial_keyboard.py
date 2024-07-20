from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData
from ..lexicon.root_lexicon import BUTTON_LEXICON


class StartTrialCallback(CallbackData, prefix="start-trial-button"):
    pass


_start_trial_button = InlineKeyboardButton(
    text=BUTTON_LEXICON["go_trial"], callback_data=StartTrialCallback().pack()
)

start_trial_keyboard = InlineKeyboardMarkup(inline_keyboard=[[_start_trial_button]])
