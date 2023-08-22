from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from modules.core.lexicon import CORE_LEXICON
from aiogram.fsm.context import FSMContext

from modules.core.states import FSMRegistration

core_router: Router = Router()


@core_router.message(CommandStart())
async def handle_start_command(message: Message, context: FSMContext):
    await message.answer(text=CORE_LEXICON['cmd_start'])

    # TODO welcome user or ask to fill username
    # context.set_state(FSMRegistration)


@core_router.message(Command('help'))
async def handle_help_command(message: Message):
    await message.answer(text=CORE_LEXICON['cmd_help'])


@core_router.message()
async def no_understand(message: Message):
    await message.answer(text=CORE_LEXICON['cannot_undertand'])
