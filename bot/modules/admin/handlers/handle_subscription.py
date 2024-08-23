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


@router.message(Command("subcription"))
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
            tg_user_id=message.from_user.id, username=username, days=days
        )

        await state.clear()
        await message.answer(
            LEXICON["subscription_success"](
                username,
                datetime.fromisoformat(subscription.until).strftime(
                    "%d.%m.%Y %H:%M:%S"
                ),
            )
        )

    except WrongSubscriptionFormatException:
        await message.answer(LEXICON["wrong_subscription_format"])
        await message.answer(LEXICON["command_subscription"])
