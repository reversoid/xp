from typing import Callable, TypedDict


class Lexicon(TypedDict):
    command_start: str
    command_subscription: str
    wrong_subscription_format: str
    subscription_success: Callable[[str, str], str]


LEXICON: Lexicon = {
    "command_start": "Привет! Это админ бот!",
    "command_subscription": "Введите имя пользователя и длительность подписки в следующем формате:\n*@username 10 days*\n\n Нажмите /cancel для отмены",
    "wrong_subscription_format": "Неверный формат",
    "subscription_success": lambda username, until: f"Успешно. Подписка для @{username} активна до {until}UTC",
}
