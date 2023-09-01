from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData


class ProfileObservationsCallback(CallbackData, prefix='profile-observations'):
    pass


class ProfileExperimentsCallback(CallbackData, prefix='profile-experiments'):
    pass


class ProfileFolloweesCallback(CallbackData, prefix='profile-followees'):
    pass


class ProfileChangeUsernameCallback(CallbackData, prefix='profile-change-username'):
    pass


class ProfileFollowCallback(CallbackData, prefix='profile-follow'):
    pass


_observations_button = InlineKeyboardButton(
    text='My Observations', callback_data=ProfileObservationsCallback().pack())

_experiments_button = InlineKeyboardButton(
    text='My Experiments', callback_data=ProfileExperimentsCallback().pack())

_followees_button = InlineKeyboardButton(
    text='My Followees', callback_data=ProfileFolloweesCallback().pack())

_follow_button = InlineKeyboardButton(
    text='Follow user', callback_data=ProfileFollowCallback().pack())

_change_username_button = InlineKeyboardButton(
    text='Change username', callback_data=ProfileChangeUsernameCallback().pack())


profile_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[_observations_button], [_experiments_button], [_followees_button], [_follow_button], [_change_username_button], ])
