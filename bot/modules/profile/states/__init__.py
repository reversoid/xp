from aiogram.filters.state import State, StatesGroup


class FSMProfile(StatesGroup):
    viewing_experiments = State()
    viewing_observations = State()
