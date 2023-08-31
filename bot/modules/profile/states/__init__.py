from aiogram.filters.state import State, StatesGroup


class FSMProfile(StatesGroup):
    sending_username_to_follow = State()
