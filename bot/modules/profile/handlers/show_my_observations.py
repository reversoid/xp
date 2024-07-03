from aiogram import Router, F, Bot
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from modules.profile.keyboards.next_observations_keyboard import (
    next_observations_keyboard,
)
from modules.profile.keyboards.profile_keyboard import ProfileObservationsCallback
from modules.profile.lexicon import LEXICON, BUTTON_LEXICON
from aiogram.fsm.context import FSMContext
from modules.profile.services import profile_service
from modules.profile.states import FSMProfile
from shared.lexicon import SHARED_LEXICON
from shared.utils.send.send_observations import send_observations

observations_router = Router()


@observations_router.message(
    StateFilter(FSMProfile.viewing_observations),
    F.text == BUTTON_LEXICON["load_more_observations"],
)
@observations_router.callback_query(ProfileObservationsCallback.filter())
async def show_observations(
    message: Message | CallbackQuery,
    state: FSMContext,
    bot: Bot,
    query: CallbackQuery | None = None,
):
    data = await state.get_data()
    lower_bound = (
        data.get("lower_bound", None)
        if isinstance(message, Message)
        and message.text == BUTTON_LEXICON["load_more_observations"]
        else None
    )

    user_id = query.from_user.id if query else message.from_user.id

    observations = await profile_service.get_user_observations(
        message.from_user.id, lower_bound
    )
    if len(observations.items) == 0:
        await bot.send_message(chat_id=user_id, text=LEXICON["empty_observations"])
        return

    (
        await bot.send_message(chat_id=user_id, text=LEXICON["your_observations"])
        if not lower_bound
        else None
    )

    await send_observations(
        bot=bot, tg_user_id=user_id, observations=observations.items
    )

    if not observations.next_key:
        await state.clear()
        await bot.send_message(
            chat_id=user_id,
            text=LEXICON["no_more_observations"],
            reply_markup=ReplyKeyboardRemove(),
        )
        return
    else:
        await state.set_state(FSMProfile.viewing_observations)
        await state.update_data(lower_bound=observations.next_key)
        await bot.send_message(
            chat_id=user_id,
            text=LEXICON["exists_more_observations"],
            reply_markup=next_observations_keyboard,
        )


@observations_router.message(
    StateFilter(FSMProfile.viewing_observations),
    F.text == BUTTON_LEXICON["cancel_showing_observations"],
)
async def cancel_show_observations(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(text=SHARED_LEXICON["ok"], reply_markup=ReplyKeyboardRemove())
