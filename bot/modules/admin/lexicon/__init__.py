from typing import Callable, TypedDict


class Lexicon(TypedDict):
    command_start: str
    command_subscription: str
    waitlist_empty: str
    waitlist_show: str
    waitlist_can_show_more: str
    wrong_subscription_format: str
    subscription_success: Callable[[str, str], str]
    canceled: str
    observation_approved: str
    observation_declined: str


LEXICON: Lexicon = {
    "command_start": "Привет! Это админ бот!",
    "command_subscription": "Введите имя пользователя и длительность подписки в следующем формате:\n\n@username 10 days\n\n Нажмите /cancel для отмены",
    "wrong_subscription_format": "Неверный формат",
    "subscription_success": lambda username, until: f"Успешно.\n\nПодписка для @{username} активна до {until}",
    "canceled": "Отменено",
    "waitlist_empty": "Нет наблюдений для подтверждения",
    "waitlist_show": "Ожидают подтверждения следующие наблюдения",
    "waitlist_can_show_more": "Есть еще наблюдения для подтверждения, загрузить?",
    "observation_approved": "Наблюдение одобрено",
    "observation_declined": "Наблюдение отклонено",
}
