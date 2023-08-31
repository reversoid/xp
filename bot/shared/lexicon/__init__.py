from typing import TypedDict


class Lexicon(TypedDict):
    internal_error: str
    ok: str


SHARED_LEXICON: Lexicon = {
    'internal_error': "Well... I am broken...",
    'ok': 'Okay'
}
