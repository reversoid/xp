from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData


class ProfileObservationsCallback(CallbackData, prefix="profile-observations"):
    cursor: str | None = None


class ProfileExperimentsCallback(CallbackData, prefix="profile-experiments"):
    cursor: str | None = None


_observations_button = InlineKeyboardButton(
    text="My Observations", callback_data=ProfileObservationsCallback().pack()
)

_experiments_button = InlineKeyboardButton(
    text="My Experiments", callback_data=ProfileExperimentsCallback().pack()
)


profile_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [_observations_button],
        [_experiments_button],
    ]
)
