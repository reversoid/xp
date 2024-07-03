from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import CommandStart
from modules.core.lexicon import CORE_LEXICON
from aiogram.fsm.context import FSMContext


from modules.auth.services import auth_service
from modules.profile.services import profile_service

start_router: Router = Router()

WELCOME_GIF_ID = (
    "CgACAgIAAxkBAAIIkWaC-mZtOFXVSZERgxKJasvkZqE4AAKoUwACyAURSFIoxT4AASK2gTUE"
)


@start_router.message(CommandStart())
async def handle_start_command(message: Message, state: FSMContext):
    await state.clear()

    tg_user_id = message.from_user.id
    tg_username = message.from_user.username

    user = await profile_service.get_user(tg_user_id)

    if not user:
        await auth_service.register(tg_user_id, tg_username)

    await message.answer_video(
        video=WELCOME_GIF_ID,
        caption=f'Привет, {tg_username} \n\n{CORE_LEXICON["cmd_start"]}',
        reply_markup=ReplyKeyboardRemove(),
    )
