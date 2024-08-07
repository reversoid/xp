from aiogram import Router, F
from aiogram.types import Message, ErrorEvent
from ..lexicon import ROOT_LEXICON
from aiogram.fsm.context import FSMContext
from aiogram.filters import ExceptionTypeFilter
from shared.middlewares.subscription_middleware import (
    ExpiredSubscriptionException,
    NoSubscriptionException,
)
from ..keyboards.buy_keyboard import buy_with_learn_more_subscription_keyboard

error_router = Router()


@error_router.error(
    ExceptionTypeFilter(ExpiredSubscriptionException), F.update.message.as_("message")
)
async def handle_my_custom_exception(event: ErrorEvent, message: Message):
    await message.answer(
        ROOT_LEXICON["subscription_expired"],
        reply_markup=buy_with_learn_more_subscription_keyboard,
    )


@error_router.error(
    ExceptionTypeFilter(NoSubscriptionException), F.update.message.as_("message")
)
async def handle_my_custom_exception(event: ErrorEvent, message: Message):
    await message.answer(
        ROOT_LEXICON["no_subscription"],
        reply_markup=buy_with_learn_more_subscription_keyboard,
    )


@error_router.error(F.update.message.as_("message"))
async def handle_exception(event: ErrorEvent, message: Message, state: FSMContext):
    print(event.exception)
    await state.clear()
    await message.answer(ROOT_LEXICON["internal_error"])
