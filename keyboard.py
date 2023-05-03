from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


button1 = KeyboardButton("/News")
keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(button1)


