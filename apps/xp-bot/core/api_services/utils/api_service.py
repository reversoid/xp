from config import load_config
from typing import Any, Dict, Optional, Type, TypeVar
import aiohttp
from pydantic import BaseModel

config = load_config()


T = TypeVar("T")

Payload = Dict[str, Any]
Headers = Dict[str, str]
Params = Dict[str, Any]


class ApiErrorResponse(BaseModel):
    message: str


class ApiException(Exception):
    status_code: int
    message: str

    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message
        super().__init__(f"HTTP error.\nStatus: {status_code}.\nMessage: {message}")


class ApiService:
    base_url = config.api.url
    api_key = config.api.api_key

    def get_url(self, path: str) -> str:
        return f"{self.base_url}/{path}"

    def get_auth_headers(self, tg_user_id: Optional[int] = None) -> Headers:
        """Generates headers to access to API

        If tg_user_id is specified, then make request for this user

        Args:
            tg_user_id (Optional[int], optional): _description_. Defaults to None.

        Returns:
            Headers: Headers to provide to request
        """
        params: Headers = {"api-key": self.api_key}
        if tg_user_id != None:
            params["tg-user-id"] = str(tg_user_id)
        return params

    async def _handle_response(
        self,
        response: aiohttp.ClientResponse,
        dataclass: Optional[Type[BaseModel]] = None,
    ):
        if not response.ok:
            error_raw = await response.text()
            error = ApiErrorResponse.model_validate_json(error_raw)
            raise ApiException(message=error.message, status_code=response.status)

        data = await response.text()
        if not data or data == "null":
            return None
        if dataclass:
            return dataclass.model_validate_json(data)
        return data

    async def get(
        self,
        url: str,
        params: Optional[Params] = None,
        dataclass: Optional[Type[BaseModel]] = None,
        headers: Optional[Headers] = None,
    ):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params, headers=headers) as response:
                return await self._handle_response(response, dataclass)

    async def post(
        self,
        url: str,
        params: Optional[Params] = None,
        dataclass: Optional[Type[BaseModel]] = None,
        payload: Optional[Payload] = None,
        headers: Optional[Headers] = None,
    ):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url, params=params, json=payload, headers=headers
            ) as response:
                return await self._handle_response(response, dataclass)

    async def put(
        self,
        url: str,
        params: Optional[Params] = None,
        dataclass: Optional[Type[BaseModel]] = None,
        payload: Optional[Payload] = None,
        headers: Optional[Headers] = None,
    ):
        async with aiohttp.ClientSession() as session:
            async with session.put(
                url, params=params, json=payload, headers=headers
            ) as response:
                return await self._handle_response(response, dataclass)

    async def patch(
        self,
        url: str,
        params: Optional[Params] = None,
        dataclass: Optional[Type[BaseModel]] = None,
        payload: Optional[Payload] = None,
        headers: Optional[Headers] = None,
    ):
        async with aiohttp.ClientSession() as session:
            async with session.patch(
                url, params=params, json=payload, headers=headers
            ) as response:
                return await self._handle_response(response, dataclass)

    async def delete(
        self,
        url: str,
        params: Optional[Params] = None,
        dataclass: Optional[Type[BaseModel]] = None,
        headers: Optional[Headers] = None,
    ):
        async with aiohttp.ClientSession() as session:
            async with session.delete(url, params=params, headers=headers) as response:
                return await self._handle_response(response, dataclass)
