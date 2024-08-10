from typing import TypedDict, Callable


class Lexicon(TypedDict):
    welcome_subscription: Callable[[str], str]
    welcome_no_subscription: Callable[[str], str]
    welcome_expired_subscription: Callable[[str], str]
    no_subscription: str
    subscription_expired: str
    about_subscription: str
    buy_subscription: str
    check_subscription_success: str
    check_subscription_failed: str
    cannot_undertand: str
    cmd_help: str
    internal_error: str


ROOT_LEXICON: Lexicon = {
    "welcome_subscription": lambda name: f"Привет {name} \n\nЭто твоя площадка для тренировки мышления. Здесь ты будешь развивать свой уникальный метод общения с миром через решение нестандартных задач \n\nДобро пожаловать в твой XP",
    "welcome_expired_subscription": lambda name: f"Привет {name} \n\n SUBSCRIPTION EXPIRED",
    "welcome_no_subscription": lambda name: f"Привет {name} \n\n WOULD LIKE TO START SUB?",
    "cmd_help": "/start - начало диалога\n/log_observation — залогировать наблюдение\n/run_experiment — провести свой эксперимент\n/profile — увидеть архив своих наблюдений и экспериментов",
    "cannot_undertand": "Непонятная команда :(",
    "internal_error": "Ошибка... Свяжитесь с создателем",
    "subscription_expired": "Кажется, у вас закончилась подписка. Для того чтобы пользоваться нужно купить...",
    "no_subscription": "Кажется, у вас нет подписки... Для того чтобы работать, надо покупать...",
    "about_subscription": "Some info about trial...",
    "buy_subscription": "Write to @anoianmari",
    "check_subscription_failed": "Пока нет подписки",
    "check_subscription_success": "Ура! Есть подписка!",
}


class ButtonLexicon(TypedDict):
    buy_subscription: str
    learn_more_subscription: str
    check_subscription: str


BUTTON_LEXICON: ButtonLexicon = {
    "buy_subscription": "Купить",
    "learn_more_subscription": "О подписке",
    "check_subscription": "Проверить",
}
