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

bot = Bot(token=token)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот вышел в онлайн')


'''Customer'''


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита')
        await message.delete()
    except:
        await message.reply('Общение с ботом только в ЛС, напишите ему: \nhttps://t.me/Restaurant_vrn_bot')


@dp.message_handler(commands=['Режим_работы'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вс-Чт с 9:00 до 24:00, Пт,Сб с 12:00 до 02:00')


@dp.message_handler(commands=['Контакты'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'г.Воронеж, ул Генерала Лизюкова д. 35 Тел. 8-952-553-73-82')


'''A common part'''


@dp.message_handler()
async def echo_send(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(" ")} \
            .intersection(set(json.load(open('censor_.json')))) != set():
        await message.reply("Мат запрещен")
        await message.delete()
    # if message.text == "Привет":
    #     await message.answer("Здравствуйте")
    # else:
    #     await message.answer("Поздоровайтесь пожалуйста")
    # await message.reply(message.text)
    # await bot.send_message(message.from_user.id, message.text)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)  # не отвечать если бот не онлайн
