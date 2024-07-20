from aiogram import Router, Bot
from aiogram.types import CallbackQuery
from modules.root.lexicon import ROOT_LEXICON
from ..keyboards.start_trial_keyboard import StartTrialCallback
from modules.subcription.services import (
    AlreadyTakenTrialException,
    subscription_service,
)

start_trial_router: Router = Router()


@start_trial_router.callback_query(StartTrialCallback.filter())
async def handle_start_trial(query: CallbackQuery, bot: Bot):
    tg_user_id = query.from_user.id

    try:
        await subscription_service.start_trial(tg_user_id)
        await bot.send_message(tg_user_id, ROOT_LEXICON["trial_success"])
        await query.message.edit_reply_markup(reply_markup=None)

    except AlreadyTakenTrialException:
        await bot.send_message(tg_user_id, ROOT_LEXICON["trial_failed"])

    finally:
        await query.answer()
