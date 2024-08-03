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
    "welcome_subscription": lambda name: f"Привет {name} \n\nЭто твоя площадка для развития мышления инноватора. Преврати этого бота в свою галерею самых красивых наблюдений и фабрику по производству креативных экспериментов.\n\nПомни, что все идеи сплетены — насыщая бота своими наблюдениями, ты обогащаешь всю сеть.\n\nHave fun. Gain more XP",
    "welcome_expired_subscription": lambda name: f"Привет {name} \n\n SUBSCRIPTION EXPIRED",
    "welcome_no_subscription": lambda name: f"Привет {name} \n\n У тебя пока нет подписки. Хочешь подключить?",
    "cmd_help": "/start - начало диалога\n/log_observation — залогировать наблюдение\n/run_experiment — провести свой эксперимент\n/profile — увидеть архив своих наблюдений и экспериментов",
    "cannot_undertand": "Непонятная команда",
    "internal_error": "Ошибка... Свяжитесь с создателем",
    "subscription_expired": "У тебя закончилась подписка — такое бывает",
    "no_subscription": "У тебя пока нет подписки",
    "about_subscription": "Подписка даёт возможность использовать бота в течение месяца. Если ты видишь это сообщение, значит, ты вытянул счастливый билет — первые два месяца твоя подписка стоит 500 рублей. Пиши @anoianmari",
    "buy_subscription": "Напиши @anoianmari",
    "check_subscription_failed": "Пока нет подписки",
    "check_subscription_success": "Отлично! Подписка в кармане",
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
