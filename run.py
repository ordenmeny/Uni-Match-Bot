import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import os
from dotenv import load_dotenv
from app.handlers import router

load_dotenv()
TOKEN = os.getenv("TOKEN")

dp = Dispatcher()


async def main():
    dp.include_router(router)
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
