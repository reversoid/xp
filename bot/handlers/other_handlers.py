from aiogram import Router
from aiogram.types import Message
from lexicon import LEXICON

router: Router = Router()


@router.message()
async def no_understand(message: Message):
    await message.answer(text=LEXICON['cannot_understand'])
