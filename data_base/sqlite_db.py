import sqlite3 as sq
from list_of_tricks import tricks
from create_bot import dp, bot


def sql_start():
    global base, cur
    base = sq.connect('bot.db')
    cur = base.cursor()
    if base:
        print('Data base conected OK!')
    base.execute('CREATE TABLE IF NOT EXISTS wake_board_tricks(type TEXT, title TEXT PRIMARY KEY,'
                 ' description TEXT, link TEXT)')
    # cur.executemany('INSERT INTO wake_board_tricks VALUES(?, ?, ?, ?)', (tricks))
    base.commit()

async def sending_tricks(message):
    for tric in cur.execute('SELECT * FROM wake_board_tricks').fetchall():

        await bot.send_message(message.from_user.id, f'{tric[1]} - {tric[2]} - {tric[-1]}')

