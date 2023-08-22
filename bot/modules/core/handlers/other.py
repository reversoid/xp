from aiogram import Router, F
from aiogram.types import Message
from modules.core.lexicon import CORE_LEXICON


other_router: Router = Router()


@other_router.message()
async def no_understand(message: Message):
    await message.answer(text=CORE_LEXICON['cannot_undertand'])
