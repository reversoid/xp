from typing import TypedDict


class Lexicon(TypedDict):
    about_profile_command: str
    send_username: str
    no_username_provided: str
    followed_successfully: str
    already_subscribed: str
    no_such_user: str
    follow_canceled: str
    your_followees: str
    empty_followees: str
    no_more_followees: str
    exists_more_followees: str


LEXICON: Lexicon = {
    'about_profile_command': 'Welcome to profile',
    'send_username': 'Send an xp-username to follow. Type /cancel to abort',
    'no_username_provided': 'Please, send a username',
    'no_such_user': 'There is no such user. Try again',
    'followed_successfully': 'You were successfully subscribed!',
    'already_subscribed': 'You are already subscribed to the user',
    'follow_canceled': 'Okay, canceled',
    'your_followees': 'The profiles you are subscribed to:',
    'empty_followees': 'There are currently no followees',
    'no_more_followees': 'There are no more followees',
    'exists_more_followees': 'There are more followees, load?'
}


class ButtonLexicon(TypedDict):
    cancel_showing_followees: str
    load_more_followees: str


BUTTON_LEXICON: ButtonLexicon = {
    'cancel_showing_followees': 'Cancel',
    'load_more_followees': 'More',
}
