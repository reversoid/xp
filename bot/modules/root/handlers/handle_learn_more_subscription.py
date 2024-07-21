from aiogram import Router, Bot
from aiogram.types import CallbackQuery
from modules.root.lexicon import ROOT_LEXICON
from ..keyboards.buy_keyboard import (
    LearnMoreSubscriptionCallback,
    buy_subscripiton_keyboard,
)


learn_more_subscription_router: Router = Router()


@learn_more_subscription_router.callback_query(LearnMoreSubscriptionCallback.filter())
async def handle_learn_more_trial(query: CallbackQuery, bot: Bot):
    tg_user_id = query.from_user.id

    try:
        await bot.send_message(
            tg_user_id,
            ROOT_LEXICON["about_subscription"],
            reply_markup=buy_subscripiton_keyboard,
        )
        await query.message.edit_reply_markup(reply_markup=None)

    finally:
        await query.answer()
