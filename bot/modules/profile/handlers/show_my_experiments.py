from aiogram import Router, Bot
from aiogram.types import CallbackQuery
from modules.profile.keyboards.next_experiments_keyboard import (
    get_next_experiments_keyboard,
)
from modules.profile.lexicon import LEXICON
from modules.profile.services import profile_service
from modules.profile.keyboards.profile_keyboard import ProfileExperimentsCallback
from shared.utils.send.send_experiments import send_experiments


experiments_router = Router()


@experiments_router.callback_query(ProfileExperimentsCallback.filter())
async def show_experiments(
    query: CallbackQuery,
    bot: Bot,
):
    cursor = (
        ProfileExperimentsCallback.unpack(query.data).cursor if query.data else None
    )

    if cursor:
        await query.message.edit_reply_markup(reply_markup=None)

    tg_user_id = query.from_user.id

    experiments = await profile_service.get_user_experiments(tg_user_id, cursor)

    if len(experiments.items) == 0:
        await bot.send_message(chat_id=tg_user_id, text=LEXICON["empty_experiments"])
        await query.answer()
        return

    if not cursor:
        await bot.send_message(chat_id=tg_user_id, text=LEXICON["your_experiments"])

    await send_experiments(
        bot=bot, tg_user_id=tg_user_id, experiments=experiments.items
    )

    if not experiments.cursor:

        await bot.send_message(
            chat_id=tg_user_id,
            text=LEXICON["no_more_experiments"],
        )
        await query.answer()

        return

    await bot.send_message(
        chat_id=tg_user_id,
        text=LEXICON["exists_more_experiments"],
        reply_markup=get_next_experiments_keyboard(experiments.cursor),
    )
    await query.answer()
