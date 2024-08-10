from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from modules.profile.lexicon import BUTTON_LEXICON
from .profile_keyboard import ProfileObservationsCallback


def _get_more_button(cursor: str):
    return InlineKeyboardButton(
        text=BUTTON_LEXICON["load_more_observations"],
        callback_data=ProfileObservationsCallback(cursor=cursor).pack(),
    )


def get_next_observations_keyboard(cursor: str):
    return InlineKeyboardMarkup(inline_keyboard=[[_get_more_button(cursor)]])
