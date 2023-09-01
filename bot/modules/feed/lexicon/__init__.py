from typing import TypedDict


class Lexicon(TypedDict):
    feed: str
    no_followee_experiments: str
    no_random_experiments: str
    showing_random: str
    followee_experiments: str
    has_more_feed: str
    no_more_feed: str
    exceeded_random_experiments: str


LEXICON: Lexicon = {
    'feed': 'This is feed. Here you can see what your followees posted recently. Or u can see random experiments from other users.',
    'no_followee_experiments': 'There are no updates for your followee',
    'showing_random': 'Lets show random experiments',
    'no_random_experiments': 'There are no available random experiments for now',
    'followee_experiments': 'Here are followee experiments',
    'has_more_feed': 'There is more feed to see, load?',
    'exceeded_random_experiments': 'There are no random experiment for now, come back in a 7 days',
    'no_more_feed': 'There is no more feed'
}


class ButtonLexicon(TypedDict):
    cancel_showing_experiments: str
    load_more_experiments: str


BUTTON_LEXICON: ButtonLexicon = {
    'cancel_showing_experiments': 'Cancel',
    'load_more_experiments': 'More'
}
