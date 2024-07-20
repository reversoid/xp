from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import CommandStart
from config.config import load_config
from modules.root.lexicon import ROOT_LEXICON
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile

from modules.auth.services import auth_service
from modules.profile.services import profile_service
from aiogram.fsm.storage.redis import Redis
from ..keyboards.trial_keyboard import start_with_learn_more_trial_keyboard
from modules.subcription.services import subscription_service

start_router: Router = Router()


FILE_ID_KEY = "welcome_file_id"

# TODO can move?
config = load_config()

redis = Redis(
    host=config.database.redis.host,
    password=config.database.redis.password,
    port=config.database.redis.port,
)


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

    existing_file_id = await redis.get(FILE_ID_KEY)
    file = (
        existing_file_id.decode()
        if existing_file_id
        else FSInputFile("static/sphere.mp4")
    )

    first_name = message.from_user.first_name
    result = await message.answer_video(
        video=file,
        caption=ROOT_LEXICON["cmd_start"](first_name),
        reply_markup=ReplyKeyboardRemove(),
    )
    if not existing_file_id:
        await redis.set(FILE_ID_KEY, result.video.file_id)

    current_subscription_status = await subscription_service.get_subscription_status(
        tg_user_id
    )

    if current_subscription_status == "EXPIRED":
        await message.answer(ROOT_LEXICON["subscription_expired"])
    elif current_subscription_status == "NO_SUBSCRIPTION":
        await message.answer(
            ROOT_LEXICON["can_trial"], reply_markup=start_with_learn_more_trial_keyboard
        )
