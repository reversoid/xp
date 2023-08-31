from aiogram.filters.state import State, StatesGroup


class FSMProfile(StatesGroup):
    sending_username_to_follow = State()
    viewing_followees = State()
    viewing_experiments = State()
    viewing_observations = State()
