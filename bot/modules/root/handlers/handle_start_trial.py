from aiogram import Router, Bot
from aiogram.types import CallbackQuery
from modules.root.lexicon import CORE_LEXICON
from ..keyboards.start_trial_keyboard import GoTrialCallback
from modules.profile.services.profile_service import (
    AlreadyTakenTrialException,
    profile_service,
)

start_trial_router: Router = Router()


@start_trial_router.callback_query(GoTrialCallback.filter())
async def handle_start_trial(query: CallbackQuery, bot: Bot):
    tg_user_id = query.from_user.id

    try:
        await profile_service.get_trial_subscription(tg_user_id)
        await bot.send_message(tg_user_id, CORE_LEXICON["trial_success"])

    except AlreadyTakenTrialException:
        await bot.send_message(tg_user_id, CORE_LEXICON["trial_success"])

    finally:
        await query.answer()
