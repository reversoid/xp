from aiogram.filters.state import State, StatesGroup


class FSMFeed(StatesGroup):
    reading_followee = State()
    reading_random = State()
