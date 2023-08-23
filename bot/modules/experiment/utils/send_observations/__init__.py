from shared.my_types import Observation
from aiogram import Bot


async def send_observations(observations: list[Observation], bot: Bot, user_id: int) -> None:
    for observation in observations:
        if observation.text:
            await bot.send_message(chat_id=user_id, text=observation.text)
        elif observation.tg_photo_id:
            await bot.send_photo(chat_id=user_id, photo=observation.tg_photo_id)
        elif observation.tg_video_id:
            await bot.send_video(chat_id=user_id, video=observation.tg_video_id)
        elif observation.tg_video_note_id:
            await bot.send_video_note(chat_id=user_id, video_note=observation.tg_video_note_id)
        elif observation.tg_document_id:
            await bot.send_document(chat_id=user_id, document=observation.tg_document_id)
        elif observation.tg_voice_id:
            await bot.send_voice(chat_id=user_id, voice=observation.tg_voice_id)
