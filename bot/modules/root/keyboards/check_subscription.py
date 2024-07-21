from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData
from ..lexicon.root_lexicon import BUTTON_LEXICON


class CheckSubscriptionCallback(CallbackData, prefix="check-subscription-button"):
    pass


_check_button = InlineKeyboardButton(
    text=BUTTON_LEXICON["check_subscription"],
    callback_data=CheckSubscriptionCallback().pack(),
)


check_subscription_keyboard = InlineKeyboardMarkup(inline_keyboard=[[_check_button]])
