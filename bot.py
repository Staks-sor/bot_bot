import asyncio
from datetime import datetime
from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from bd.count_bd import get_connect_heroku_bd
from config.config_token import TOKEN
from config.config_token import WETHER_TOKEN
from des.des import *
from generator.generator import *
from markup import markup as nav
from wether.wether import open_wether

bot = Bot(token=TOKEN)
loop = asyncio.get_event_loop()
dp = Dispatcher(bot, storage=MemoryStorage(), loop=loop)
dp.middleware.setup(LoggingMiddleware())
f = open('../botmyffff/bd/index.txt', "r")
number_id = f.read(1)
f.close()
index = int(number_id)
print(index, "Это индекс")
print("Фаил закрыт")


class Form(StatesGroup):
    city = State()
    gor = State()


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Привет {0.first_name}! \n Я бот для развлечения(пока только для развлечения)'.format(
                               message.from_user),
                           reply_markup=nav.mainMenu)
    chat_id = 459830083
    time_user = datetime.now()
    await bot.send_message(chat_id, message.from_user.username + ": " + message.text[6:] + str(time_user.hour))


@dp.message_handler(commands=['faq'])
async def process_start_command(message: types.Message):
    await message.reply(faq)


@dp.message_handler(commands=['author'])
async def process_start_command(message: types.Message):
    await message.reply(author)


@dp.message_handler(Text(equals='Регистрация'))
async def regestration_commands(message: types.Message):
    if message.text == 'Регистрация':
        await bot.send_message(message.from_user.id, 'В ближайщем обновлении',
                               reply_markup=nav.mainMenu)


@dp.message_handler(Text(equals='Полезное'))
async def polza_commands(message: types.Message):
    if message.text == 'Полезное':
        await bot.send_message(message.from_user.id, 'Выбери погоду и введи город',
                               reply_markup=nav.wetherMenu)


@dp.message_handler(Text(equals='Полезное'))
async def whether_commands(message: types.Message):
    if message.text == 'Погода':
        await bot.send_message(message.from_user.id,
                               'Погода',
                               reply_markup=nav.wetherMenu)


@dp.message_handler(Text(equals='Узнать погоду'))
async def whether_pol_commands(message: types.Message):
    if message.text == "Узнать погоду":
        await Form.city.set()
        await message.reply("Привет! Напиши мне название города и я пришлю сводку погоды!")


@dp.message_handler(Text(equals='Развлечения'))
async def happy_commands(message: types.Message):
    if message.text == 'Развлечения':
        await bot.send_message(message.from_user.id, 'Генерация мата, бредовый гороскоп',
                               reply_markup=nav.otherMenu)


@dp.message_handler(Text(equals='Мат'))
async def mat_commands(message: types.Message):
    if message.text == 'Мат':
        await bot.send_message(message.from_user.id, 'Мат',
                               reply_markup=nav.matMenu)


@dp.message_handler(Text(equals='Для парня'))
async def mat_man_commands(message: types.Message):
    if message.text == 'Для парня':
        await message.answer(for_man())


@dp.message_handler(Text(equals='Для девушки'))
async def mat_woman_commands(message: types.Message):
    if message.text == 'Для девушки':
        await message.answer(for_women())


@dp.message_handler(Text(equals='Главное меню'))
async def main_commands(message: types.Message):
    if message.text == 'Главное меню':
        await bot.send_message(message.from_user.id, 'Главное меню',
                               reply_markup=nav.mainMenu)


@dp.message_handler(Text(equals='Гороскоп'))
async def gor_commands(message: types.Message):
    if message.text == 'Гороскоп':
        await bot.send_message(message.from_user.id, 'Гороскоп', reply_markup=nav.goroskop_menu)


@dp.message_handler(Text(equals='Получить гороскоп'))
async def main_commands(message: types.Message):
    if message.text == 'Получить гороскоп':
        await message.reply("Введите свой знак зодиака")
        await Form.gor.set()


@dp.message_handler(state=Form.gor)
async def zodiac_commands(message: types.Message, state: FSMContext):
    if message.text == 'Главное меню':
        await bot.send_message(message.from_user.id, 'Главное меню',
                               reply_markup=nav.mainMenu)
        await state.finish()
    else:
        async with state.proxy() as data:
            try:
                data['zoc'] = message.text
                zoc = data['zoc']
                goro = get_connect_heroku_bd(zodiac=zoc.capitalize(), id=index)

                await message.reply(goro)
                chat_id = 459830083
                time_user = datetime.now()
                await bot.send_message(chat_id,
                                       message.from_user.username + ": " + message.text[6:] + str(time_user.hour))
            except Exception:
                await message.reply("Что блядь знаки зодиака не знаем?")

        await state.finish()


@dp.message_handler(state=Form.city)
async def process_name(message: types.Message, state: FSMContext):
    if message.text == 'Главное меню':
        await bot.send_message(message.from_user.id, 'Главное меню',
                               reply_markup=nav.mainMenu)
        await state.finish()
    else:
        async with state.proxy() as data:
            data['city'] = message.text
            city = data['city']
            res = open_wether(city, WETHER_TOKEN)
            await message.answer(res)

        await state.finish()


async def sending_messages():
    global index
    while True:
        time_now = datetime.now()
        print(time_now.hour)
        if time_now.hour == 4:
            index += 1
            f1 = open('../botmyffff/bd/index.txt', "w")
            f1.write(str(index))
            print('Сменил значение')
            f1.close()
            await asyncio.sleep(3600)
        await asyncio.sleep(1)

if __name__ == '__main__':
    dp.loop.create_task(sending_messages())
    executor.start_polling(dp, skip_updates=True)
