from aiogram import Router, F, Bot
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, ReplyKeyboardRemove
from modules.experiment.utils.send_experiments import send_experiments
from modules.profile.keyboards.next_experiments_keyboard import next_experiments_keyboard
from modules.profile.lexicon import LEXICON, BUTTON_LEXICON
from aiogram.fsm.context import FSMContext
from modules.profile.services import profile_service
from modules.profile.states import FSMProfile
from shared.lexicon import SHARED_LEXICON

experiments_router = Router()


@experiments_router.message(Command('my_experiments'))
@experiments_router.message(StateFilter(FSMProfile.viewing_experiments), F.text == BUTTON_LEXICON['load_more_experiments'])
async def show_experiments(message: Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    lower_bound = data.get(
        'lower_bound', None) if message.text == BUTTON_LEXICON['load_more_experiments'] else None

    experiments = await profile_service.get_my_experiments(message.from_user.id, lower_bound)
    if (len(experiments.items) == 0):
        await message.answer(text=LEXICON['empty_experiments'])
        return

    await message.answer(text=LEXICON['your_experiments']) if not lower_bound else None

    await send_experiments(bot=bot, tg_user_id=message.from_user.id, experiments=experiments.items)

    if not experiments.next_key:
        await state.clear()
        await message.answer(text=LEXICON['no_more_experiments'], reply_markup=ReplyKeyboardRemove())
        return
    else:
        await state.set_state(FSMProfile.viewing_experiments)
        await state.update_data(lower_bound=experiments.next_key)
        await message.answer(text=LEXICON['exists_more_experiments'], reply_markup=next_experiments_keyboard)


@experiments_router.message(StateFilter(FSMProfile.viewing_experiments), F.text == BUTTON_LEXICON['cancel_showing_experiments'])
async def cancel_show_experiments(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(text=SHARED_LEXICON['ok'], reply_markup=ReplyKeyboardRemove())
