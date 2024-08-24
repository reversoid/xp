from aiogram.filters.state import State, StatesGroup


class FSMAdminSubscription(StatesGroup):
    filling = State()


class FSMAdminWaitlist(StatesGroup):
    showing = State()
