from aiogram import Bot
from aiogram.types import BotCommand
from modules.root.lexicon.menu_commands import MENU_COMMANDS


async def set_main_menu(bot: Bot) -> None:
    main_menu_commands = [
        BotCommand(command=command, description=description)
        for command, description in MENU_COMMANDS.items()
    ]

    await bot.set_my_commands(main_menu_commands)
