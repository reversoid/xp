from aiogram.filters.state import State, StatesGroup


class FSMRegistration(StatesGroup):
    fill_username = State()
