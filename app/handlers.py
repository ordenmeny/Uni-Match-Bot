import os
from traceback import print_tb

from aiogram.filters import CommandStart, CommandObject, Command
from aiogram.types import Message, BotCommand
from aiogram import F, Router
from dotenv import load_dotenv
from .api_requests import *
from .keyboards import *

load_dotenv()
HOST = os.getenv("HOST")

router = Router()


@router.message(CommandStart(deep_link=True))
async def start_handler(message: Message, command: CommandObject):
    if command.args[0:6] == "login_":
        uniq_code = command.args[6:]
        try:
            answer = await set_uniq_code_by_chat_id(message.chat.id, uniq_code)
            if answer is None:
                raise Exception("Не удалось установить уникальный код для чата.")
        except Exception as e:
            logging.error(e)

    else:
        uniq_code = command.args
        answer = await set_chat_id(str(message.chat.id), str(uniq_code))
        if answer:
            await message.answer("Теперь ваш аккаунт привязан к боту.", reply_markup=main_kb)
        else:
            await message.answer("Что-то пошло не так.")


@router.message(CommandStart())
async def start_handler(message: Message, command: CommandObject):
    user = None
    try:
        user = await get_user(message.chat.id)
    except Exception as e:
        await message.answer(f"Ошибка")

    if user is None:
        await message.answer(f'Привет. Сначала авторизуйся на сайте:', reply_markup=firsr_kb)
    else:
        await message.answer(f'Выберите действие:', reply_markup=main_kb)
