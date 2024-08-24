from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData


class AdminApproveObservationCallback(CallbackData, prefix="admin-approve-observation"):
    observation_id: str


class AdminDeleteObservationCallback(CallbackData, prefix="admin-delete-observation"):
    observation_id: str


class AdminShowMoreWaitlistCallback(CallbackData, prefix="admin-show-more-waitlist"):
    cursor: str | None = None


def _get_approve_button(observation_id: str):
    return InlineKeyboardButton(
        text="Одобрить",
        callback_data=AdminApproveObservationCallback(
            observation_id=observation_id
        ).pack(),
    )


def _get_delete_button(observation_id: str):
    return InlineKeyboardButton(
        text="Отклонить",
        callback_data=AdminDeleteObservationCallback(
            observation_id=observation_id
        ).pack(),
    )


def get_manage_observation_keyboard(observation_id: str):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [_get_delete_button(observation_id)],
            [_get_approve_button(observation_id)],
        ]
    )


def _get_show_more_button(cursor: str):
    return InlineKeyboardButton(
        text="Загрузить больше",
        callback_data=AdminShowMoreWaitlistCallback(cursor=cursor).pack(),
    )


def get_show_more_waitlist_keyboard(cursor: str):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [_get_show_more_button(cursor)],
        ]
    )
