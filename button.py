from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


sherik = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text="Sherik kerak"),KeyboardButton(text="Ustoz kerak")],
        [KeyboardButton(text="Shogird kerak"),KeyboardButton(text="Ish joyi kerak")],
    ],
    resize_keyboard=True
)