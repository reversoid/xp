from config_data import load_config
from typing import Any, Dict, Optional, Type, TypeVar, Protocol, Union
import aiohttp

config = load_config()


T = TypeVar('T')

Payload = Dict[str, Any]


class DataClassJSON(Protocol):
    def __init__(self, **data: Any) -> None: pass


class ApiService:
    base_url = config.api.url
    api_secret = config.api.api_secret

    async def get(self, url: str, dataclass: Optional[Type[T]] = None) -> Union[T, Any]:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                data = await response.json()
                if dataclass:
                    return dataclass(**data)
                return data

    async def post(self, url: str, dataclass: Optional[Type[T]] = None, payload: Optional[Payload] = None) -> Union[T, Any]:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as response:
                response.raise_for_status()
                data = await response.json()
                return dataclass(**data) if dataclass else data

    async def put(self, url: str, dataclass: Optional[Type[T]] = None, payload: Optional[Payload] = None) -> Union[T, Any]:
        async with aiohttp.ClientSession() as session:
            async with session.put(url, json=payload) as response:
                response.raise_for_status()
                data = await response.json()
                return dataclass(**data) if dataclass else data

    async def patch(self, url: str, dataclass: Optional[Type[T]] = None, payload: Optional[Payload] = None) -> Union[T, Any]:
        async with aiohttp.ClientSession() as session:
            async with session.patch(url, json=payload) as response:
                response.raise_for_status()
                data = await response.json()
                return dataclass(**data) if dataclass else data

    async def delete(self, url: str, dataclass: Optional[Type[T]] = None) -> Union[T, Any]:
        async with aiohttp.ClientSession() as session:
            async with session.delete(url) as response:
                response.raise_for_status()
                data = await response.json()
                return dataclass(**data) if dataclass else data