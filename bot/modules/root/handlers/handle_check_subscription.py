from aiogram import Router, Bot
from aiogram.types import CallbackQuery
from modules.root.lexicon import ROOT_LEXICON
from modules.subcription.services import subscription_service
from ..keyboards.check_subscription import (
    CheckSubscriptionCallback,
    check_subscription_keyboard,
)


check_subscription_router: Router = Router()


@check_subscription_router.callback_query(CheckSubscriptionCallback.filter())
async def handle_check_subscription(query: CallbackQuery, bot: Bot):
    tg_user_id = query.from_user.id
    subscription_status = await subscription_service.get_subscription_status(tg_user_id)

    await query.message.edit_reply_markup(reply_markup=None)

    if subscription_status == "ACTIVE":
        await bot.send_message(
            tg_user_id, text=ROOT_LEXICON["check_subscription_success"]
        )
    else:
        await bot.send_message(
            tg_user_id,
            text=ROOT_LEXICON["check_subscription_failed"],
            reply_markup=check_subscription_keyboard,
        )

    await query.answer()
