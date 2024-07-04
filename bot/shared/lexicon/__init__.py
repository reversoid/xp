from typing import TypedDict


class Lexicon(TypedDict):
    ok: str
    canceled: str


SHARED_LEXICON: Lexicon = {"ok": "Окэй", "canceled": "Отменено"}
