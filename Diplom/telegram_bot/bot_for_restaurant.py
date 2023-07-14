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


@dp.message_handler()
async def echo_send(message: types.Message):
    await message.answer(message.text)
    # await message.reply(message.text)
    # await bot.send_message(message.from_user.id, message.text)


executor.start_polling(dp, skip_updates=True)  # не отвечать если бот не онлайн
