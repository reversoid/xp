from core.models import Observation
from aiogram import Bot
from .send_media_group import send_media_group


async def send_observations(
    observations: list[Observation], bot: Bot, tg_user_id: int
) -> None:
    for observation in observations:
        if observation.tgPhotoId:
            await bot.send_photo(
                chat_id=tg_user_id,
                photo=observation.tgPhotoId,
                caption=observation.tgText,
            )
        elif observation.tgVideoId:
            await bot.send_video(
                chat_id=tg_user_id,
                video=observation.tgVideoId,
                caption=observation.tgText,
            )
        elif observation.tgVideoNoteId:
            await bot.send_video_note(
                chat_id=tg_user_id, video_note=observation.tgVideoNoteId
            )
        elif observation.tgDocumentId:
            await bot.send_document(
                chat_id=tg_user_id,
                document=observation.tgDocumentId,
                caption=observation.tgText,
            )
        elif observation.tgVoiceId:
            await bot.send_voice(
                chat_id=tg_user_id,
                voice=observation.tgVoiceId,
                caption=observation.tgText,
            )
        elif observation.tgMediaGroup:
            await send_media_group(
                tg_user_id=tg_user_id,
                media_group=observation.tgMediaGroup,
                text=observation.tgText,
                bot=bot,
            )
        elif observation.tgText:
            await bot.send_message(chat_id=tg_user_id, text=observation.tgText)
