from typing import TypedDict


class Lexicon(TypedDict):
    log_observation: str
    log_observation_success: str
    not_supported_data: str
    send_one_item: str


LEXICON: Lexicon = {
    'log_observation': """
        Your observation could take any form: a word, a screenshot, a manifesto, a voice memo or a 2-second video shot.
        What made you curious today?
    """,

    'log_observation_success': 'Your observation is logged.',

    'not_supported_data': """
        I cannot understand this type of data.
        Your observation could take any form: a word, a screenshot, a manifesto, a voice memo or a 2-second video shot.
    """,

    'send_one_item': 'Please, send one item'
}
