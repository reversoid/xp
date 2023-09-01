from aiogram import Router, F, Bot
from aiogram.filters import StateFilter
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from modules.experiment.utils.send_experiments import send_experiments
from modules.profile.keyboards.next_experiments_keyboard import next_experiments_keyboard
from modules.profile.lexicon import LEXICON, BUTTON_LEXICON
from aiogram.fsm.context import FSMContext
from modules.profile.services import profile_service
from modules.profile.states import FSMProfile
from shared.lexicon import SHARED_LEXICON
from modules.profile.keyboards.profile_keyboard import ProfileExperimentsCallback

experiments_router = Router()


@experiments_router.callback_query(ProfileExperimentsCallback.filter())
@experiments_router.message(StateFilter(FSMProfile.viewing_experiments), F.text == BUTTON_LEXICON['load_more_experiments'])
async def show_experiments(message: Message | CallbackQuery, bot: Bot, state: FSMContext,  query: CallbackQuery | None = None):
    data = await state.get_data()
    lower_bound = data.get(
        'lower_bound', None) if isinstance(message, Message) and message.text == BUTTON_LEXICON['load_more_experiments'] else None

    user_id = query.from_user.id if query else message.from_user.id

    experiments = await profile_service.get_my_experiments(user_id, lower_bound)
    if (len(experiments.items) == 0):
        await bot.send_message(chat_id=user_id, text=LEXICON['empty_experiments'])
        return

    await bot.send_message(chat_id=user_id, text=LEXICON['your_experiments']) if not lower_bound else None

    await send_experiments(bot=bot, tg_user_id=user_id, experiments=experiments.items)

    if not experiments.next_key:
        await state.clear()
        await bot.send_message(chat_id=user_id, text=LEXICON['no_more_experiments'], reply_markup=ReplyKeyboardRemove())
        return
    else:
        await state.set_state(FSMProfile.viewing_experiments)
        await state.update_data(lower_bound=experiments.next_key)
        await bot.send_message(chat_id=user_id, text=LEXICON['exists_more_experiments'], reply_markup=next_experiments_keyboard)


@experiments_router.message(StateFilter(FSMProfile.viewing_experiments), F.text == BUTTON_LEXICON['cancel_showing_experiments'])
async def cancel_show_experiments(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(text=SHARED_LEXICON['ok'], reply_markup=ReplyKeyboardRemove())
