from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from modules.profile.lexicon import BUTTON_LEXICON
from .profile_keyboard import ProfileExperimentsCallback


def _get_more_button(cursor: str):
    return InlineKeyboardButton(
        text=BUTTON_LEXICON["load_more_experiments"],
        callback_data=ProfileExperimentsCallback(cursor=cursor),
    )


def get_next_experiments_keyboard(cursor: str):
    return InlineKeyboardMarkup(inline_keyboard=[[_get_more_button(cursor)]])
