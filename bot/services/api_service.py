from config_data import load_config
from typing import Any, Dict, Optional, Type, TypeVar, Protocol, Union
import aiohttp
from pydantic import BaseModel

config = load_config()


T = TypeVar('T')

Payload = Dict[str, Any]
Headers = Dict[str, str]
Params = Dict[str, Any]


class DataClassJSON(Protocol):
    def __init__(self, **data: Any) -> None: pass


class ApiService:
    base_url = config.api.url
    api_secret = config.api.api_secret

    def get_auth_headers(self, tg_user_id: Optional[int] = None) -> Headers:
        """Generates headers to access to API

        If tg_user_id is specified, then make request for this user

        Args:
            tg_user_id (Optional[int], optional): _description_. Defaults to None.

        Returns:
            Headers: Headers to provide to request
        """
        params: Headers = {'secret_key': self.api_secret}
        if tg_user_id != None:
            params['tg_user_id'] = str(tg_user_id)
        return params

    async def get(self, url: str, params: Optional[Params] = None, dataclass: Optional[Type[BaseModel]] = None, headers: Optional[Headers] = None):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params, headers=headers) as response:
                response.raise_for_status()
                data = await response.text()
                if dataclass:
                    return dataclass.parse_raw(data)
                return data

    async def post(self, url: str, params: Optional[Params] = None, dataclass: Optional[Type[BaseModel]] = None, payload: Optional[Payload] = None, headers: Optional[Headers] = None):
        async with aiohttp.ClientSession() as session:
            async with session.post(url, params=params, json=payload, headers=headers) as response:
                response.raise_for_status()
                data = await response.text()
                if dataclass:
                    return dataclass.parse_raw(data)
                return data

    async def put(self, url: str, params: Optional[Params] = None, dataclass: Optional[Type[BaseModel]] = None, payload: Optional[Payload] = None, headers: Optional[Headers] = None):
        async with aiohttp.ClientSession() as session:
            async with session.put(url, params=params, json=payload, headers=headers) as response:
                response.raise_for_status()
                data = await response.text()
                if dataclass:
                    return dataclass.parse_raw(data)
                return data

    async def patch(self, url: str, params: Optional[Params] = None, dataclass: Optional[Type[BaseModel]] = None, payload: Optional[Payload] = None, headers: Optional[Headers] = None):
        async with aiohttp.ClientSession() as session:
            async with session.patch(url, params=params, json=payload, headers=headers) as response:
                response.raise_for_status()
                data = await response.text()
                if dataclass:
                    return dataclass.parse_raw(data)
                return data

    async def delete(self, url: str, params: Optional[Params] = None, dataclass: Optional[Type[BaseModel]] = None, headers: Optional[Headers] = None):
        async with aiohttp.ClientSession() as session:
            async with session.delete(url, params=params, headers=headers) as response:
                response.raise_for_status()
                data = await response.text()
                if dataclass:
                    return dataclass.parse_raw(data)
                return data
