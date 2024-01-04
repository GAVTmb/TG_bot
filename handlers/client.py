from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from data_base import sqlite_db

# @dp.message_handler(commands=['Бот', 'бот'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привет райдер! Чем могу помочь?', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с Ботом в личных сообщениях, напишите ему:\nhttps://t.me/Wake_Up68Bot')

async def list_of_tricks(message: types.Message):
    await sqlite_db.sending_tricks(message)


def reg_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(list_of_tricks, commands=['Трюки'])
