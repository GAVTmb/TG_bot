from aiogram import types, Dispatcher
from create_bot import dp, bot
import json, string


async def reading_messages(message: types.Message):
    print(message.text.split(' '))
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('search_list.json')))) != set():
        await message.reply('Узнать о проведении тренеровок и записаться можно через нашего Бота'
                            ', напишите ему:\nhttps://t.me/Wake_Up68Bot')
        await bot.send_message(message.from_user.id, 'Привет райдер! Чем могу помочь?')


def reg_handlers_others(dp: Dispatcher):
    dp.register_message_handler(reading_messages)
