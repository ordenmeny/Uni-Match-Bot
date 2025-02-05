from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from .api_requests import HOST

firsr_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Авторизоваться", url=f"{HOST}/users/signup")]
])


kb_dict = {"main": "Главная", "profile": "Профиль"}

main_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=kb_dict["main"]), KeyboardButton(text=kb_dict["profile"])],
], resize_keyboard=True)
