from typing import TypedDict


class Lexicon(TypedDict):
    experiment_started: str
    confirm_experiment: str
    continue_experiment: str
    success_experiment: str
    no_text_in_experiment: str
    cancel_experiment: str
    experiment_not_started: str
    experiment_already_started: str
    not_enough_observations: str
    experiment_expired: str


LEXICON: Lexicon = {
    "experiment_started": """
        У тебя есть 24 часа. Затем прикрепи своё решение в формате:\n—Название эксперимента\n—Артефакты результата \n—Артефакты процесса, если хочешь
    """,
    "confirm_experiment": """
        Цель — придумать задачу, основанную на трех наблюдениях других людей, и поделиться своим решением. У тебя будет на это 24 часа. Если хочешь, прикрепи также документацию процесса\n\nГотовность?
    """,
    "success_experiment": "Удачно!",
    "no_text_in_experiment": "У эксперимента должно быть хотя бы название. Добавь в сообщение текст",
    "experiment_not_started": "Эксперимент не начат или уже завершился. Начни новый /run_experiment",
    "experiment_already_started": "Эксперимент уже начат",
    "not_enough_observations": "Пока в сети недостаточно наблюдений, чтобы начать эксперементировать..",
    "experiment_expired": "Этот эксперимент истёк. Чтобы начать новый, жми /run_experiment",
}


class ButtonLexicon(TypedDict):
    cancel: str
    finish: str


BUTTON_LEXICON: ButtonLexicon = {"cancel": "Отменить", "finish": "Завершить"}
