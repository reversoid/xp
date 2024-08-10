from aiogram import Router, Bot
from aiogram.types import ReplyKeyboardRemove, CallbackQuery
from modules.profile.keyboards.next_observations_keyboard import (
    get_next_observations_keyboard,
)
from modules.profile.keyboards.profile_keyboard import ProfileObservationsCallback
from modules.profile.lexicon import LEXICON
from modules.profile.services import profile_service
from shared.utils.send.send_observations import send_observations

observations_router = Router()


@observations_router.callback_query(ProfileObservationsCallback.filter())
async def show_observations(
    query: CallbackQuery,
    bot: Bot,
):
    cursor = (
        ProfileObservationsCallback.unpack(query.data).cursor if query.data else None
    )

    if cursor and query.message:
        await query.message.edit_reply_markup(reply_markup=None)

    tg_user_id = query.from_user.id

    observations = await profile_service.get_user_observations(tg_user_id, cursor)

    if len(observations.items) == 0:
        await bot.send_message(chat_id=tg_user_id, text=LEXICON["empty_observations"])
        await query.answer()
        return

    if not cursor:
        await bot.send_message(chat_id=tg_user_id, text=LEXICON["your_observations"])

    await send_observations(
        bot=bot, tg_user_id=tg_user_id, observations=observations.items
    )

    if not observations.cursor:

        await bot.send_message(
            chat_id=tg_user_id,
            text=LEXICON["no_more_observations"],
            reply_markup=ReplyKeyboardRemove(),
        )
        await query.answer()
        return

    await bot.send_message(
        chat_id=tg_user_id,
        text=LEXICON["exists_more_observations"],
        reply_markup=get_next_observations_keyboard(observations.cursor),
    )
    await query.answer()
