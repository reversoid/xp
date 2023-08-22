from aiogram.types import Message
from shared.types import GeoDTO, MediaGroupItemDTO, UploadInfoRequest


def process_media_group_files(messages: list[Message]) -> UploadInfoRequest:
    text = ''
    media_group: list[MediaGroupItemDTO] = []
    for message in messages:
        if message.text:
            text = f'{text} {message.text}'
        if message.caption:
            text = f'{text} {message.caption}'
        audio_id = message.audio.file_id if message.audio else None
        document_id = message.document.file_id if message.document else None
        photo_id = message.photo[-1].file_id if message.photo else None
        video_id = message.video.file_id if message.video else None
        media_group_item = MediaGroupItemDTO(
            audio_id=audio_id, document_id=document_id, photo_id=photo_id, video_id=video_id)
        media_group.append(media_group_item)
    request = UploadInfoRequest(
        text=text if text else None, media_group=media_group)
    return request


def process_message_files(message: Message) -> UploadInfoRequest:
    document_id = message.document.file_id if message.document else None
    text = message.text
    photo_id = message.photo[-1].file_id if message.photo else None
    video_id = message.video.file_id if message.video else None
    video_note_id = message.video_note.file_id if message.video_note else None
    voice_id = message.voice.file_id if message.voice else None
    geo = GeoDTO(longitude=message.location.longitude,
                 latitude=message.location.latitude, horizontal_accuracy=message.location.horizontal_accuracy) if message.location else None

    request = UploadInfoRequest(
        document_id=document_id, text=text, photo_id=photo_id, video_id=video_id, video_note_id=video_note_id, voice_id=voice_id, geo=geo)
    return request
