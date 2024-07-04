from typing import TypedDict, Callable


class Lexicon(TypedDict):
    welcome_profile: Callable[[str], str]
    empty_experiments: str
    no_more_experiments: str
    your_experiments: str
    exists_more_experiments: str
    empty_observations: str
    no_more_observations: str
    your_observations: str
    exists_more_observations: str


LEXICON: Lexicon = {
    "welcome_profile": lambda username: f"Hello, {username}!",
    "empty_experiments": "No experiments yet",
    "no_more_experiments": "There are no more experiments",
    "your_experiments": "Here are your experiments",
    "exists_more_experiments": "There are more experiments, load?",
    "empty_observations": "No observations yet",
    "no_more_observations": "There are no more observations",
    "your_observations": "Here are your observations",
    "exists_more_observations": "There are more observations, load?",
}


class ButtonLexicon(TypedDict):
    load_more_experiments: str
    load_more_observations: str


BUTTON_LEXICON: ButtonLexicon = {
    "load_more_experiments": "More",
    "load_more_observations": "More",
}
