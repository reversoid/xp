from typing import Callable, TypedDict


class Lexicon(TypedDict):
    experiment_started: str
    confirm_experiment: str
    success_experiment: str
    no_text_in_experiment: str
    experiment_not_started: str
    experiment_already_started: str
    not_enough_observations: str
    experiment_expired: str
    experiment_will_expire: Callable[[int], str]
    experiment_canceled: str


LEXICON: Lexicon = {
    "experiment_started": """
        У тебя есть 24 часа. Затем прикрепи своё решение в формате:\n—Название эксперимента\n—Артефакты результата \n—Артефакты процесса, если хочешь \n\nДля отмены эксперимента введи: /cancel
    """,
    "confirm_experiment": """
        Цель — придумать задачу, основанную на трех наблюдениях других людей, и поделиться своим решением. У тебя будет на это 24 часа. Результат эксперимента должен быть отправлен одним сообщением. Если хочешь, прикрепи также документацию процесса\n\nГотовность?
    """,
    "success_experiment": "Удачно!",
    "no_text_in_experiment": "У эксперимента должно быть хотя бы название. Добавь в сообщение текст",
    "experiment_not_started": "Эксперимент не начат или уже завершился. Начни новый /run_experiment",
    "experiment_already_started": "Эксперимент уже начат",
    "not_enough_observations": "Пока в сети недостаточно наблюдений, чтобы начать эксперементировать..",
    "experiment_expired": "Этот эксперимент истёк. Чтобы начать новый, жми /run_experiment",
    "experiment_will_expire": lambda time: f"Эксперимент закончится через {time}ч",
    "experiment_canceled": "Эксперимент отменен",
}


class ButtonLexicon(TypedDict):
    start: str


BUTTON_LEXICON: ButtonLexicon = {"start": "Готовность"}
