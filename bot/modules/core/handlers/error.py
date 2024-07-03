from aiogram import Router, F
from aiogram.types import Message, ErrorEvent
from ..lexicon import CORE_LEXICON

error_router = Router()


@error_router.error(F.update.message.as_("message"))
async def handle_exception(event: ErrorEvent, message: Message):
    print(event.exception)
    await message.answer(CORE_LEXICON["internal_error"])
