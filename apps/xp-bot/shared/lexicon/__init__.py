from typing import TypedDict


class Lexicon(TypedDict):
    canceled: str


SHARED_LEXICON: Lexicon = {"canceled": "Отменено"}
