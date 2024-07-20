from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData
from ..lexicon.root_lexicon import BUTTON_LEXICON


class StartTrialCallback(CallbackData, prefix="start-trial-button"):
    pass


class LearnMoreTrialCallback(CallbackData, prefix="learn-more-trial-button"):
    pass


_start_trial_button = InlineKeyboardButton(
    text=BUTTON_LEXICON["go_trial"], callback_data=StartTrialCallback().pack()
)

_learn_more_trial_button = InlineKeyboardButton(
    text=BUTTON_LEXICON["learn_more_trial"],
    callback_data=LearnMoreTrialCallback().pack(),
)

start_trial_keyboard = InlineKeyboardMarkup(inline_keyboard=[[_start_trial_button]])

start_with_learn_more_trial_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[_start_trial_button], [_learn_more_trial_button]]
)
