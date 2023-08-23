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
    'experiment_started': """
        You have 24 hours to run an experiment. Then upload it in the following format:
        — Experiment Name
        — Result Artefacts
        — Process Artefacts if desired
    """,

    'confirm_experiment': """
        The goal is to make up a task based on 3 observations of others and share your solution. You will have 24 hours. Add process artefacts if desired.
        Ready?
    """,

    'continue_experiment': 'I got it. \n\n Continue?',

    'success_experiment': 'Success!',

    'no_text_in_experiment': 'No text in experiment... Provide it please',

    'cancel_experiment': 'You cancelled the experiment',

    'experiment_not_started': 'Experiment is not started',

    'experiment_already_started': 'Experiment is already started',

    'not_enough_observations': 'Not enough observations to continue... please wait for more!',

    'experiment_expired': 'Your experiment expired! Just start a new one'
}


class ButtonLexicon(TypedDict):
    cancel: str
    finish: str


BUTTON_LEXICON: ButtonLexicon = {
    'cancel': 'Cancel',
    'finish': 'Finish'
}
