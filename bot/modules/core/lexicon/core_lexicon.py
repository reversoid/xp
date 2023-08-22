from typing import TypedDict


class Lexicon(TypedDict):
    cannot_undertand: str
    internal_error: str
    cmd_start: str
    cmd_help: str


CORE_LEXICON: Lexicon = {
    'cmd_start': 'Hello!',

    'cmd_help': 'This is what this bot can do:',

    'cannot_undertand': "I do not understand :(",

    # TODO internal error is like shared stuff... Can we make it shared?
    'internal_error': "Ohh, I have a problem... Please, contact the creator to fix me!",
}
