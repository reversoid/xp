from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData
from ..lexicon.core_lexicon import BUTTON_LEXICON


class GoTrialCallback(CallbackData, prefix="go-trial-button"):
    pass


_go_trial_button = InlineKeyboardButton(
    text=BUTTON_LEXICON["go_trial"], callback_data=GoTrialCallback().pack()
)

go_trial_keyboard = InlineKeyboardMarkup(inline_keyboard=[[_go_trial_button]])
