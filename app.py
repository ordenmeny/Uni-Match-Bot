import asyncio
import logging
import sys
import aiohttp
from aiogram import Bot, Dispatcher, html, types, F
from aiogram.client import bot
from aiogram.client.default import DefaultBotProperties
from aiogram.dispatcher import router
from aiogram.enums import ParseMode, ContentType
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import FSInputFile
from aiogram.utils.deep_linking import decode_payload
from aiogram.filters import CommandStart, CommandObject
from aiogram.types import Message
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

dp = Dispatcher()

IP = "127.0.0.1:8000"


async def set_chat_id(chat_id, uniq_code):
    url = f"http://127.0.0.1:8000/users/api/get-bot/{uniq_code}/"
    data = {
        "uniq_code": "",
        "chat_id": chat_id
    }

    async with aiohttp.ClientSession() as session:
        async with session.patch(url, json=data) as response:
            if response.status in (200, 201):
                result = await response.json()
                return result
            else:
                error_message = await response.text()
                return None


@dp.message(CommandStart(deep_link=True))
async def start_handler(message: Message, command: CommandObject):
    uniq_code = command.args
    answer = await set_chat_id(str(message.chat.id), str(uniq_code))
    if answer:
        await message.answer("Теперь ваш аккаунт привязан к боту")
    else:
        await message.answer("Что-то пошло не так :(")



async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
