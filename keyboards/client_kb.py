from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

c1 = KeyboardButton('Пообщатся_с_ботом')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(c1)
