from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db


async def on_startup(_):
    print('Бот онлайн!')
    sqlite_db.sql_start()


from handlers import client, admin, other

client.reg_handlers_client(dp)
other.reg_handlers_others(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
