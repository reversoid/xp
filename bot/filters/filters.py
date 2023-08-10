from typing import Any
from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery
import re


class IsDigitCallbackData(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        return isinstance(callback.data, str) and callback.data.isdigit()


_delete_callback_query_pattern = r'\d+ del'


def _is_delete_pattern(str: str):
    return bool(re.search(_delete_callback_query_pattern, str))


class IsDelBookmarkCallbackData(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        return isinstance(callback.data, str) and _is_delete_pattern(callback.data)
