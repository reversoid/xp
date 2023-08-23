from aiogram import Router
from aiogram.filters import Command, StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from modules.experiment.lexicon import LEXICON
from modules.experiment.states import FSMExperiment
from shared.utils.convert.message_to_upload_request import process_message_files
from shared.my_types import UploadInfoRequest

router: Router = Router()


@router.message(StateFilter(FSMExperiment.completing))
async def handle_experiment(message: Message, state: FSMContext):
    data = await state.get_data()
    # TODO apply middleware that reveals media group 
    messages: list[UploadInfoRequest] = data.get('messages', [])
    newRequest = process_message_files(message)
    messages.append(newRequest.model_dump())

    await state.update_data(messages=messages)
    await message.answer(text=LEXICON['continue_experiment'])
    # TODO check for maximim messages length (should not be greater than 10)
