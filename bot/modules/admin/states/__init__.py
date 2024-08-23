from aiogram.filters.state import State, StatesGroup


class FSMSubscription(StatesGroup):
    filling = State()
