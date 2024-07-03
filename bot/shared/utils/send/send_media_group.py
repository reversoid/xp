from aiogram import Bot
from core.models import TgMediaGroupItem
from aiogram.types import (
    InputMediaAudio,
    InputMediaDocument,
    InputMediaPhoto,
    InputMediaVideo,
)

MediaGroupItem = (
    InputMediaAudio | InputMediaDocument | InputMediaPhoto | InputMediaVideo
)


async def send_media_group(
    tg_user_id: int, media_group: list[TgMediaGroupItem], text: str | None, bot: Bot
):
    media: list[MediaGroupItem] = []

    for item in media_group:
        caption = text if not caption_added else None
        caption_added = True

        if item.tgAudioId:
            media.append(InputMediaAudio(media=item.tgAudioId, caption=caption))

        if item.tgPhotoId:
            media.append(InputMediaPhoto(media=item.tgPhotoId, caption=caption))

        if item.tgVideoId:
            media.append(InputMediaVideo(media=item.tgVideoId, caption=caption))

        if item.tgDocumentId:
            media.append(InputMediaDocument(media=item.tgDocumentId, caption=caption))

    await bot.send_media_group(chat_id=tg_user_id, media=media)
