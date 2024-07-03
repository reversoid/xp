from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from modules.core.middlewares.AlbumMiddleware import AlbumMiddleware

from modules.experiment.lexicon import LEXICON
from modules.experiment.states import FSMExperiment


router: Router = Router()

router.message.middleware.register(AlbumMiddleware())


@router.message(StateFilter(FSMExperiment.completing), F.media_group_id == None)
async def handle_experiment(message: Message, state: FSMContext):
    data = await state.get_data()
    messages: list[UploadInfoRequest] = data.get("messages", [])
    newRequest = process_message_files(message)
    messages.append(newRequest.model_dump())

    await state.update_data(messages=messages)
    await message.answer(text=LEXICON["continue_experiment"])
    # TODO check for maximim messages length (should not be greater than 10)


@router.message(StateFilter(FSMExperiment.completing), F.media_group_id != None)
async def handle_media_group(message: Message, state: FSMContext, album: list[Message]):
    data = await state.get_data()
    messages: list[UploadInfoRequest] = data.get("messages", [])
    newRequest = process_media_group_files(album)
    messages.append(newRequest.model_dump())

    await state.update_data(messages=messages)
    await message.answer(text=LEXICON["continue_experiment"])
    # TODO check for maximim messages length (should not be greater than 10)
