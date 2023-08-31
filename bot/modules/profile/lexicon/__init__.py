from typing import TypedDict


class Lexicon(TypedDict):
    about_profile_command: str
    send_username: str
    no_username_provided: str
    followed_successfully: str
    already_subscribed: str
    no_such_user: str


LEXICON: Lexicon = {
    'about_profile_command': 'Welcome to profile',
    'send_username': 'Send an xp-username to follow',
    'no_username_provided': 'Please, send a username',
    'no_such_user': 'There is no such user. Try again',
    'followed_successfully': 'You were successfully subscribed!',
    'already_subscribed': 'You are already subscribed to the user',
}
