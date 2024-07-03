from .other import other_router
from .handle_start_command import start_router as _start_router
from .help import help_router
from aiogram import Router, F
from aiogram.filters import ExceptionTypeFilter
from aiogram.types import Message
from ..lexicon.core_lexicon import CORE_LEXICON

core_router = Router()

core_router.include_routers(_start_router, help_router)


@core_router.error(ExceptionTypeFilter(Exception), F.update.message.as_("message"))
async def handle_my_custom_exception(message: Message):
    await message.answer(CORE_LEXICON)
