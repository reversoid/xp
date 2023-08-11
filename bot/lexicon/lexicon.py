from typing import TypedDict


class Lexicon(TypedDict):
    cmd_start: str
    cmd_help: str
    cannot_understand: str
    internal_error: str
    start_experiment: str
    confirm_experiment: str


LEXICON: Lexicon = {
    'cmd_start': 'Hello!',
    'cmd_help': 'Help',
    'cannot_understand': 'I cannot understand...',
    'internal_error': 'Something went wrong... Try again, please',
    'start_experiment': """
    You have 24 hours to run an experiment. Then upload it in the following format:
    — Experiment Name
    — Result Artefacts
    — Process Artefacts if desired
    """,
    'confirm_experiment': """
        The goal is to make up a task based on 3 observations of others and share your solution. You will have 24 hours. Add process artefacts if desired.
        Ready?
    """
}
