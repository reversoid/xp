from core.api_services.experiment_api_service.exceptions import (
    AlreadyStartedExperimentException,
    NoActiveExperimentException,
)
from core.models import Experiment, Observation
from core.api_services.observation_api_service import observation_api_service
from core.api_services.experiment_api_service import (
    experiment_api_service,
    CompleteExperimentDto,
)
from core.models import TgGeo
from .exceptions import (
    NotEnoughObservationsException,
    NoTextInExperimentDtoException,
    NotStartedExperimentException,
)
from .exceptions import AlreadyStartedExperimentException as AlreadyStartedException
from aiogram.types import Message
from core.models import TgMediaGroupItem

OBSERVATIONS_AMOUNT_TO_START_EXPERIMENT = 3


class ExperimentService:
    async def get_current_experiment(self, tg_user_id: int):
        return experiment_api_service.get_user_current_experiment(tg_user_id)

    async def get_observations_for_experiment(self, tg_user_id: int):
        observations = await observation_api_service.get_random_observations(
            tg_user_id, OBSERVATIONS_AMOUNT_TO_START_EXPERIMENT
        )

        if len(observations) < OBSERVATIONS_AMOUNT_TO_START_EXPERIMENT:
            raise NotEnoughObservationsException

        return observations

    async def mark_observations_as_seen(
        self, tg_user_id: int, observations: list[Observation]
    ):
        for o in observations:
            await observation_api_service.mark_observation_as_viewed(tg_user_id, o.id)

    async def create_experiment(self, tg_user_id: int) -> Experiment:
        try:
            experiment: Experiment = await experiment_api_service.start_experiment(
                tg_user_id
            )

            return experiment

        except AlreadyStartedExperimentException:
            raise AlreadyStartedException

    async def complete_experiment(
        self, tg_user_id: int, messages: list[Message]
    ) -> Experiment:
        dto: CompleteExperimentDto

        if len(messages) == 1:
            message = messages[0]
            text = message.text or message.caption
            video_id = message.video.file_id if message.video else None
            photo_id = message.photo[-1].file_id if message.photo else None
            document_id = message.document.file_id if message.document else None
            geo = (
                TgGeo(
                    longitude=message.location.longitude,
                    latitude=message.location.latitude,
                    horizontalAccuracy=message.location.horizontal_accuracy,
                )
                if message.location
                else None
            )
            voice_id = message.voice.file_id if message.voice else None
            video_note_id = message.video_note.file_id if message.video_note else None
            dto = CompleteExperimentDto(
                tgText=text,
                tgPhotoId=photo_id,
                tgVideoId=video_id,
                tgDocumentId=document_id,
                tgGeo=geo,
                tgVoiceId=voice_id,
                tgVideoNoteId=video_note_id,
                tgMediaGroup=None,
            )

        else:  # For media group
            text = ""
            media_group: list[TgMediaGroupItem] = []

            for message in messages:
                text += message.text or message.caption
                media_group_item = TgMediaGroupItem(
                    tgAudioId=message.audio.file_id,
                    tgDocumentId=message.document.file_id,
                    tgPhotoId=message.photo[-1].file_id,
                    tgVideoId=message.video.file_id,
                )
                media_group.append(media_group_item)

            dto = CompleteExperimentDto(tgText=text, tgMediaGroup=media_group_item)

        self.__validate_complete_experiment_dto(dto)
        try:

            experiment = await experiment_api_service.complete_experiment(
                tg_user_id, dto
            )
            return experiment
        except NoActiveExperimentException:
            raise NotStartedExperimentException

    def __validate_complete_experiment_dto(self, dto: CompleteExperimentDto):
        if not dto.tgText:
            raise NoTextInExperimentDtoException


experiment_service = ExperimentService()
