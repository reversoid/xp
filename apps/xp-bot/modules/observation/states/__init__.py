from aiogram.filters.state import State, StatesGroup


class FSMObservation(StatesGroup):
    completing = State()
