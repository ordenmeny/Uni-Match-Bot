import aiohttp
from aiogram.filters import CommandStart, CommandObject, Command
from aiogram.types import Message
from aiogram import F, Router
from .api_requests import set_chat_id

router = Router()


@router.message(CommandStart(deep_link=True))
async def start_handler(message: Message, command: CommandObject):
    uniq_code = command.args
    answer = await set_chat_id(str(message.chat.id), str(uniq_code))
    if answer:
        await message.answer("Теперь ваш аккаунт привязан к боту.")
    else:
        await message.answer("Что-то пошло не так.")


@router.message(Command("hello"))
async def hello_handler(message: Message):
    await message.answer(f"Hello")
