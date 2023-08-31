from aiogram import Router, F, Bot
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, ReplyKeyboardRemove
from modules.experiment.utils.send_observations import send_observations
from modules.experiment.utils.send_experiments import send_experiments
from modules.profile.keyboards.next_observations_keyboard import next_observations_keyboard
from modules.profile.lexicon import LEXICON, BUTTON_LEXICON
from aiogram.fsm.context import FSMContext
from modules.profile.services import profile_service
from modules.profile.states import FSMProfile
from shared.lexicon import SHARED_LEXICON

observations_router = Router()


@observations_router.message(Command('my_observations'))
@observations_router.message(StateFilter(FSMProfile.viewing_experiments), F.text == BUTTON_LEXICON['load_more_observations'])
async def show_experiments(message: Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    lower_bound = data.get(
        'lower_bound', None) if message.text == BUTTON_LEXICON['load_more_observations'] else None

    observations = await profile_service.get_my_observations(message.from_user.id, lower_bound)
    if (len(observations.items) == 0):
        await message.answer(text=LEXICON['empty_observations'])
        return

    await message.answer(text=LEXICON['your_observations']) if not lower_bound else None

    await send_observations(bot=bot, tg_user_id=message.from_user.id, observations=observations.items)

    if not observations.next_key:
        await state.clear()
        await message.answer(text=LEXICON['no_more_observations'], reply_markup=ReplyKeyboardRemove())
        return
    else:
        await state.set_state(FSMProfile.viewing_observations)
        await state.update_data(lower_bound=observations.next_key)
        await message.answer(text=LEXICON['exists_more_observations'], reply_markup=next_observations_keyboard)


@observations_router.message(StateFilter(FSMProfile.viewing_experiments), F.text == BUTTON_LEXICON['cancel_showing_observations'])
async def cancel_show_observations(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(text=SHARED_LEXICON['ok'], reply_markup=ReplyKeyboardRemove())
