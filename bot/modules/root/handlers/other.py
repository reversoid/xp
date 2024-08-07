from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove
from modules.root.lexicon import ROOT_LEXICON


other_router: Router = Router()


@other_router.message()
async def no_understand(message: Message):
    await message.answer(
        text=ROOT_LEXICON["cannot_undertand"], reply_markup=ReplyKeyboardRemove()
    )
