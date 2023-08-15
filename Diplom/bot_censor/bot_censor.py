import string
import json

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

with open("token.txt", "r") as file1:
    # итерация по строкам
    token = ""
    for line in file1:
        token = line

proxy_url = 'http://proxy.server:3128'
bot = Bot(token=token, proxy=proxy_url)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот вышел в онлайн')


@dp.message_handler()
async def echo_send(message: types.Message):
    try:
        if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(" ")} \
                .intersection(set(json.load(open('censor_.json')))) != set():
            await message.reply("Мат запрещен")
            await message.delete()
    except:
        await message.reply('Я даже не понял, что вы ввели')


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)  # не отвечать если бот не онлайн
