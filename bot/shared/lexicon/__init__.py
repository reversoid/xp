from typing import TypedDict


class Lexicon(TypedDict):
    internal_error: str
    ok: str


SHARED_LEXICON: Lexicon = {
    "internal_error": "У меня возникла ошибка. Свяжитесь с",
    "ok": "Окэй",
}
