from typing import TypedDict


class Lexicon(TypedDict):
    experiment_started: str
    confirm_experiment: str


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
}
