from aiogram import Router, Bot
from aiogram.types import CallbackQuery
from modules.root.lexicon import ROOT_LEXICON
from ..keyboards.buy_keyboard import BuySubscriptionCallback
from ..keyboards.check_subscription import check_subscription_keyboard

buy_subscription_router: Router = Router()


@buy_subscription_router.callback_query(BuySubscriptionCallback.filter())
async def handle_buy_subscription(query: CallbackQuery, bot: Bot):
    tg_user_id = query.from_user.id

    try:
        await bot.send_message(
            tg_user_id,
            ROOT_LEXICON["buy_subscription"],
            reply_markup=check_subscription_keyboard,
        )
        await query.message.edit_reply_markup(reply_markup=None)

    finally:
        await query.answer()
