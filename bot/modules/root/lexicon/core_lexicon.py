from typing import TypedDict


class Lexicon(TypedDict):
    cannot_undertand: str
    cmd_start: str
    cmd_help: str
    internal_error: str
    subscription_expired: str
    can_trial: str
    trial_success: str
    trial_failed: str


CORE_LEXICON: Lexicon = {
    "cmd_start": "Это твоя площадка для тренировки мышления. Здесь ты будешь развивать свой уникальный метод общения с миром через решение нестандартных задач \n\nДобро пожаловать в твой XP",
    "cmd_help": "/start - начало диалога\n/log_observation — залогировать наблюдение\n/run_experiment — провести свой эксперимент\n/profile — увидеть архив своих наблюдений и экспериментов",
    "cannot_undertand": "Непонятная команда :(",
    "internal_error": "Ошибка... Свяжитесь с создателем",
    "subscription_expired": "Кажется, у вас закончилась подписка. Хотите продолжить? Напишите...",
    "can_trial": "У вас нет подписки, хотите начать пробный период?",
    "trial_success": "Вы оформили пробную подписку на 7 дней",
    "trial_failed": "Вы уже оформляли пробную подписку :(",
}


class ButtonLexicon(TypedDict):
    go_trial: str


BUTTON_LEXICON: ButtonLexicon = {"go_trial": "Вперед!"}
