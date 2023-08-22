from typing import TypedDict


class Lexicon(TypedDict):
    internal_error: str


SHARED_LEXICON: Lexicon = {
    'internal_error': "Ohh, I have a problem... Please, contact the creator to fix me!",
}
