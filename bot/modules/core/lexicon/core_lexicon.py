from typing import TypedDict


class Lexicon(TypedDict):
    cannot_undertand: str
    cmd_start: str
    cmd_help: str
    fill_username: str
    welcome: str
    username_already_taken: str
    bad_username_message: str
    wrong_username_format: str


CORE_LEXICON: Lexicon = {
    'cmd_start': 'This bot can do a lot of things...',

    'cmd_help': 'This is what this bot can do...',

    'cannot_undertand': "I do not understand :(",

    'fill_username': 'Please, input your username',

    'welcome': 'Welcome!',

    'username_already_taken': 'This username is already taken... \n\n Try to send another one.',

    'bad_username_message': 'I need your username, please...',

    'wrong_username_format': 'This is not format of usernames... it should be...'
}
