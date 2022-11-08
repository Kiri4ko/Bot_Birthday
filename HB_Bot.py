"""Bot Coin API v.1.0.0. Connected to the API cryptocurrencies market"""

import config

import asyncio

import logging

from handlers.callback import register_callback
from handlers.start import register_handlers_common
from handlers.quiz import register_handlers_quiz
from filters.filters import register_handlers_filters

from aiogram.types.bot_command import BotCommand

from aiogram.contrib.fsm_storage.memory import MemoryStorage

from aiogram import Bot, Dispatcher

from aiogram import types

logger = logging.getLogger(__name__)


# commands registration

async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Принять поздравления 🎁"),
        BotCommand(command="/cancel", description="Отменить текущее действие 🛑")
    ]
    await bot.set_my_commands(commands)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    # declaring and initializing bot and dispatcher objects

    bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.MARKDOWN_V2)
    dp = Dispatcher(bot, storage=MemoryStorage())

    # handler Registration

    register_callback(dp)
    register_handlers_common(dp)
    register_handlers_quiz(dp)
    register_handlers_filters(dp)

    # bot commands installation

    await set_commands(bot)

    # launching Polling
    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
