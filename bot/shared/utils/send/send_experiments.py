from core.models import Experiment
from aiogram import Bot
from .send_media_group import send_media_group


async def send_experiments(
    experiments: list[Experiment], bot: Bot, tg_user_id: int
) -> None:
    for experiment in experiments:
        if experiment.tgPhotoId:
            await bot.send_photo(
                chat_id=tg_user_id,
                photo=experiment.tgPhotoId,
                caption=experiment.tgText,
            )
        elif experiment.tgVideoId:
            await bot.send_video(
                chat_id=tg_user_id,
                video=experiment.tgVideoId,
                caption=experiment.tgText,
            )
        elif experiment.tgVideoNoteId:
            await bot.send_video_note(
                chat_id=tg_user_id, video_note=experiment.tgVideoNoteId
            )
        elif experiment.tgDocumentId:
            await bot.send_document(
                chat_id=tg_user_id,
                document=experiment.tgDocumentId,
                caption=experiment.tgText,
            )
        elif experiment.tgVoiceId:
            await bot.send_voice(
                chat_id=tg_user_id,
                voice=experiment.tgVoiceId,
                caption=experiment.tgText,
            )
        elif experiment.tgMediaGroup:
            await send_media_group(
                tg_user_id=tg_user_id,
                media_group=experiment.tgMediaGroup,
                text=experiment.tgText,
                bot=bot,
            )
        elif experiment.tgText:
            await bot.send_message(chat_id=tg_user_id, text=experiment.tgText)
