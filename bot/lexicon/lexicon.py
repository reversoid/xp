from typing import TypedDict


class Lexicon(TypedDict):
    cmd_start: str
    cmd_help: str
    cannot_understand: str
    internal_error: str
    start_experiment: str
    confirm_experiment: str
    log_observation: str
    log_observation_success: str


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
    """,
    'log_observation': """Your observation could take any form: a word, a screenshot, a manifesto, a voice memo or a 2-second video shot. 

What made you curious today?""",
    'log_observation_success': 'Your observation is logged.'
}
