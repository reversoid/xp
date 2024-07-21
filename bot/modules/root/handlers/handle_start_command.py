from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from config.config import load_config
from modules.root.lexicon import ROOT_LEXICON
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, InlineKeyboardMarkup

from modules.auth.services import auth_service
from modules.profile.services import profile_service
from aiogram.fsm.storage.redis import Redis
from ..keyboards.buy_keyboard import (
    buy_subscripiton_keyboard,
    buy_with_learn_more_subscription_keyboard,
)
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


async def send_welcome_text(
    message: Message, text: str, reply_markup: InlineKeyboardMarkup = None
):
    existing_file_id = await redis.get(FILE_ID_KEY)
    file = (
        existing_file_id.decode()
        if existing_file_id
        else FSInputFile("static/sphere.mp4")
    )

    sent_message = await message.answer_video(
        video=file,
        caption=text,
        reply_markup=reply_markup,
    )

    if not existing_file_id:
        await redis.set(FILE_ID_KEY, sent_message.video.file_id)


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

    current_subscription_status = await subscription_service.get_subscription_status(
        tg_user_id
    )

    first_name = message.from_user.first_name
    if current_subscription_status == "ACTIVE":
        await send_welcome_text(
            message=message, text=ROOT_LEXICON["welcome_subscription"](first_name)
        )
    elif current_subscription_status == "EXPIRED":
        await send_welcome_text(
            message=message,
            text=ROOT_LEXICON["welcome_expired_subscription"](first_name),
            reply_markup=buy_subscripiton_keyboard,
        )
    elif current_subscription_status == "NO_SUBSCRIPTION":
        await send_welcome_text(
            message=message,
            text=ROOT_LEXICON["welcome_no_subscription"](first_name),
            reply_markup=buy_with_learn_more_subscription_keyboard,
        )
