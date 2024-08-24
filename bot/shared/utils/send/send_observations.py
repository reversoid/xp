from core.models import Observation
from aiogram import Bot
from .send_media_group import send_media_group
from aiogram.types import InlineKeyboardMarkup


async def send_observation(
    observation: Observation,
    bot: Bot,
    tg_user_id: int,
    reply_markup: InlineKeyboardMarkup = None,
):
    if observation.tgPhotoId:
        await bot.send_photo(
            chat_id=tg_user_id,
            photo=observation.tgPhotoId,
            caption=observation.tgText,
            reply_markup=reply_markup,
        )
    elif observation.tgVideoId:
        await bot.send_video(
            chat_id=tg_user_id,
            video=observation.tgVideoId,
            caption=observation.tgText,
            reply_markup=reply_markup,
        )
    elif observation.tgVideoNoteId:
        await bot.send_video_note(
            chat_id=tg_user_id,
            video_note=observation.tgVideoNoteId,
            reply_markup=reply_markup,
        )
    elif observation.tgDocumentId:
        await bot.send_document(
            chat_id=tg_user_id,
            document=observation.tgDocumentId,
            caption=observation.tgText,
            reply_markup=reply_markup,
        )
    elif observation.tgVoiceId:
        await bot.send_voice(
            chat_id=tg_user_id,
            voice=observation.tgVoiceId,
            caption=observation.tgText,
            reply_markup=reply_markup,
        )
    elif observation.tgMediaGroup:
        await send_media_group(
            tg_user_id=tg_user_id,
            media_group=observation.tgMediaGroup,
            text=observation.tgText,
            bot=bot,
            reply_markup=reply_markup,
        )
    elif observation.tgText:
        await bot.send_message(
            chat_id=tg_user_id, text=observation.tgText, reply_markup=reply_markup
        )


async def send_observations(
    observations: list[Observation],
    bot: Bot,
    tg_user_id: int,
    reply_markup: InlineKeyboardMarkup = None,
) -> None:
    for observation in observations:
        await send_observation(observation, bot, tg_user_id, reply_markup)
