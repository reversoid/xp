from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import CommandStart
from modules.core.lexicon import CORE_LEXICON
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile

from modules.auth.services import auth_service
from modules.profile.services import profile_service

start_router: Router = Router()


@start_router.message(CommandStart())
async def handle_start_command(
    message: Message,
    state: FSMContext,
):

    await state.clear()

    tg_user_id = message.from_user.id
    tg_username = message.from_user.username

    user = await profile_service.get_user(tg_user_id)

    if not user:
        await auth_service.register(tg_user_id, tg_username)

    # TODO cache file id
    file = FSInputFile("static/sphere.mp4")

    result = await message.answer_video(
        video=file,
        caption=f'Привет, {tg_username} \n\n{CORE_LEXICON["cmd_start"]}',
        reply_markup=ReplyKeyboardRemove(),
    )
