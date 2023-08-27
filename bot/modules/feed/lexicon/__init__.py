from typing import TypedDict


class Lexicon(TypedDict):
    no_followee_experiments: str
    no_random_experiments: str
    showing_random: str


LEXICON: Lexicon = {
    'no_followee_experiments': 'There are no updates for your followee',
    'showing_random': 'Lets show random experiments',
    'no_random_experiments': 'There are no random experiment for now, come back in a 7 days.'
}
