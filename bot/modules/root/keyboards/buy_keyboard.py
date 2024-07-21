from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData
from ..lexicon.root_lexicon import BUTTON_LEXICON


class BuySubscriptionCallback(CallbackData, prefix="buy-subscription-button"):
    pass


class LearnMoreSubscriptionCallback(
    CallbackData, prefix="learn-more-subscription-button"
):
    pass


_buy_button = InlineKeyboardButton(
    text=BUTTON_LEXICON["buy_subscription"],
    callback_data=BuySubscriptionCallback().pack(),
)

_learn_more_button = InlineKeyboardButton(
    text=BUTTON_LEXICON["learn_more_subscription"],
    callback_data=LearnMoreSubscriptionCallback().pack(),
)

buy_subscripiton_keyboard = InlineKeyboardMarkup(inline_keyboard=[[_buy_button]])

buy_with_learn_more_subscription_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[_buy_button], [_learn_more_button]]
)
