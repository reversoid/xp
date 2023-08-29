from shared.my_types import Experiment, MediaGroupItem
from aiogram import Bot
from shared.utils.convert.experiment_to_media_group import experiment_to_media_group_with_text


async def send_experiments(experiments: list[Experiment], bot: Bot, tg_user_id: int):
    for experiment in experiments:
        media_group, text = experiment_to_media_group_with_text(experiment)

        if len(media_group) >= 2:
            media_group[0].caption = text
            await bot.send_media_group(chat_id=tg_user_id, media=media_group)
        elif len(media_group) == 1:
            if experiment.tg_photo_id:
                await bot.send_photo(chat_id=tg_user_id, caption=text, photo=experiment.tg_photo_id)

            elif experiment.tg_document_id:
                await bot.send_document(chat_id=tg_user_id, caption=text, document=experiment.tg_document_id)

            elif experiment.tg_video_id:
                await bot.send_video(chat_id=tg_user_id, caption=text, video=experiment.tg_video_id)

            elif experiment.tg_video_note_id:
                await bot.send_video_note(chat_id=tg_user_id, caption=text, video_note=experiment.tg_video_note_id)

            elif experiment.tg_voice_id:
                await bot.send_voice(chat_id=tg_user_id, caption=text, video_note=experiment.tg_voice_id)
        elif text:
            await bot.send_message(chat_id=tg_user_id, text=text)
