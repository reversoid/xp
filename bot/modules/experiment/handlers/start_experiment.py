from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from modules.experiment.lexicon import LEXICON
from modules.experiment.keyboards import confirm_start_experiment_keyboard
from modules.experiment.services import experiment_service
from modules.experiment.states import FSMExperiment

router: Router = Router()


@router.message(Command("run_experiment"))
async def handle_start_experiment(message: Message, state: FSMContext):
    currentExperiment = await experiment_service.get_current_experiment(
        tg_user_id=message.from_user.id
    )

    if currentExperiment:
        await message.answer(text=LEXICON["experiment_already_started"])
        await message.answer(text=LEXICON["experiment_started"])
        await state.set_state(FSMExperiment.completing)

    else:
        await message.answer(
            text=LEXICON["confirm_experiment"],
            reply_markup=confirm_start_experiment_keyboard,
        )
