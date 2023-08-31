from shared.my_types import Experiment, MediaGroupItem
from aiogram.types import InputMediaAudio, InputMediaDocument, InputMediaPhoto, InputMediaVideo


def experiment_to_media_group_with_text(experiment: Experiment) -> tuple[list[MediaGroupItem] | None, str]:
    text = experiment.text
    media_group: list[MediaGroupItem] = []

    if not experiment.tg_media_group:
        return [], text

    for media_group_item in experiment.tg_media_group:
        if media_group_item.audio_id:
            media_group.append(InputMediaAudio(
                media=media_group_item.audio_id))

        if media_group_item.photo_id:
            media_group.append(InputMediaPhoto(
                media=media_group_item.photo_id))

        if media_group_item.video_id:
            media_group.append(InputMediaVideo(
                media=media_group_item.video_id))

        if media_group_item.document_id:
            media_group.append(InputMediaDocument(
                media=media_group_item.document_id))

    return media_group[:10], text
