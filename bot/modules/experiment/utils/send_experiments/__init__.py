from modules.feed.keyboards.follow_keyboard import get_follow_keyboard
from shared.my_types import Experiment
from aiogram import Bot
from aiogram.types import InlineKeyboardMarkup
from shared.utils.convert.experiment_to_media_group import experiment_to_media_group_with_text


async def send_experiments(experiments: list[Experiment], bot: Bot, tg_user_id: int, include_subscribe_markup: bool = False):
    for experiment in experiments:
        media_group, text = experiment_to_media_group_with_text(experiment)
        keyboard: InlineKeyboardMarkup | None = None
        if include_subscribe_markup:
            keyboard = get_follow_keyboard(experiment.user.id)

        if len(media_group) >= 2:
            await bot.send_media_group(chat_id=tg_user_id, media=media_group)
            await bot.send_message(chat_id=tg_user_id, text='', reply_markup=keyboard) if include_subscribe_markup else None
        elif len(media_group) == 1:
            if experiment.tg_photo_id:
                await bot.send_photo(chat_id=tg_user_id, caption=text, photo=experiment.tg_photo_id, reply_markup=keyboard)

            elif experiment.tg_document_id:
                await bot.send_document(chat_id=tg_user_id, caption=text, document=experiment.tg_document_id, reply_markup=keyboard)

            elif experiment.tg_video_id:
                await bot.send_video(chat_id=tg_user_id, caption=text, video=experiment.tg_video_id, reply_markup=keyboard)

            elif experiment.tg_video_note_id:
                await bot.send_video_note(chat_id=tg_user_id, caption=text, video_note=experiment.tg_video_note_id, reply_markup=keyboard)

            elif experiment.tg_voice_id:
                await bot.send_voice(chat_id=tg_user_id, caption=text, reply_markup=keyboard, video_note=experiment.tg_voice_id)
        elif text:
            await bot.send_message(chat_id=tg_user_id, text=text, reply_markup=keyboard)
