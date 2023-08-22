from shared.types import UploadInfoRequest
from shared.utils.convert.message_to_upload_request import process_message_files
from .exceptions import NoDataForObservation
from shared.api_service import ApiService, Payload
from aiogram.types import Message


class ObservationService(ApiService):
    async def create_observation(self, tg_user_id: int, message: Message):
        url = f'{self.base_url}/observations'
        request = self.__get_request_for_creation_observation(message)
        headers = self.get_auth_headers(tg_user_id)
        await self.post(url, payload=request, headers=headers)

    def __get_request_for_creation_observation(self, message: Message) -> Payload:
        request = process_message_files(message)
        self.__validate_created_observation(request)

        return request.model_dump()

    def __validate_created_observation(self, request: UploadInfoRequest):
        if not request.text and not request.photo_id and not request.video_id and not request.voice_id and not request.video_note_id:
            raise NoDataForObservation

observation_service = ObservationService()