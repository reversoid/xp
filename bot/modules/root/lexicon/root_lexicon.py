from typing import TypedDict, Callable


class Lexicon(TypedDict):
    cannot_undertand: str
    welcome_subscription: Callable[[str], str]
    welcome_no_subscription: Callable[[str], str]
    welcome_expired_subscription: Callable[[str], str]
    cmd_help: str
    internal_error: str
    subscription_expired: str
    can_trial: str
    about_trial: str
    trial_success: str
    trial_failed: str


ROOT_LEXICON: Lexicon = {
    "welcome_subscription": lambda name: f"Привет {name} \n\nЭто твоя площадка для тренировки мышления. Здесь ты будешь развивать свой уникальный метод общения с миром через решение нестандартных задач \n\nДобро пожаловать в твой XP",
    "welcome_expired_subscription": lambda name: f"Привет {name} \n\n SUBSCRIPTION EXPIRED",
    "welcome_no_subscription": lambda name: f"Привет {name} \n\n WOULD LIKE TO START SUB?",
    "cmd_help": "/start - начало диалога\n/log_observation — залогировать наблюдение\n/run_experiment — провести свой эксперимент\n/profile — увидеть архив своих наблюдений и экспериментов",
    "cannot_undertand": "Непонятная команда :(",
    "internal_error": "Ошибка... Свяжитесь с создателем",
    "subscription_expired": "Кажется, у вас закончилась подписка. Хотите продолжить? Напишите...",
    "can_trial": "У вас нет подписки, хотите начать пробный период?",
    "trial_success": "Вы оформили пробную подписку на 7 дней",
    "trial_failed": "Вы уже оформляли пробную подписку :(",
    "about_trial": "Some info about trial...",
}


class ButtonLexicon(TypedDict):
    go_trial: str
    learn_more_trial: str


BUTTON_LEXICON: ButtonLexicon = {
    "go_trial": "Вперед!",
    "learn_more_trial": "О подписке",
}
