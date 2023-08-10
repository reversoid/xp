from enum import Enum
from typing import TypedDict


class Lexicon(TypedDict):
    cmd_start: str
    cmd_help: str
    cannot_understand: str


LEXICON: Lexicon = {
    'cmd_start': 'Hello!',
    'cmd_help': 'Help',
    'cannot_understand': 'I cannot understand...'
}
