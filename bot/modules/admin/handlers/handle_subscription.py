from datetime import datetime
from aiogram import Router
from aiogram.filters import Command, StateFilter
from aiogram.types import Message
from modules.admin.lexicon import LEXICON
from aiogram.fsm.context import FSMContext
from modules.admin.states import FSMSubscription
from modules.admin.utils.parse_subscription_text import (
    WrongSubscriptionFormatException,
    parse_subscription_text,
)
from modules.admin.services import admin_service

router: Router = Router()


@router.message(Command("subscription"))
async def command_subscription(
    message: Message,
    state: FSMContext,
):
    await state.set_state(FSMSubscription.filling)
    await message.answer(LEXICON["command_subscription"])


@router.message(StateFilter(FSMSubscription.filling))
async def handle_input_subscription(
    message: Message,
    state: FSMContext,
):
    try:
        username, days = parse_subscription_text(message.text)
        subscription = await admin_service.upsert_subscription(
            message.from_user.id, username, days
        )

        await state.clear()
        await message.answer(
            LEXICON["subscription_success"](
                username,
                subscription.until.strftime("%d.%m.%Y %H:%M:%S") + " UTC",
            )
        )

    except WrongSubscriptionFormatException:
        await message.answer(LEXICON["wrong_subscription_format"])
        await message.answer(LEXICON["command_subscription"])
