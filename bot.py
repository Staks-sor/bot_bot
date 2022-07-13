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
from bd.count_bd import get_connect_heroku_bd, get_id, get_id_index, user_reg, user_examination
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

index = int(get_id_index())
print(index, "Это индекс")


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
    await bot.send_message(chat_id, message.from_user.username, "заходил какой то чел")


@dp.message_handler(commands=['faq'])
async def process_start_command(message: types.Message):
    await message.reply(faq)


@dp.message_handler(commands=['author'])
async def process_start_command(message: types.Message):
    await message.reply(author)


@dp.message_handler(Text(equals='Войти'))
async def regestration_commands(message: types.Message):
    if message.text == 'Войти':
        if not user_examination(message.from_user.id):
            user_reg(message.from_user.first_name, int(message.from_user.id))
            await bot.send_message(message.from_user.id, "Вы вошли в личный кабинет", reply_markup=nav.menu_personal)
        else:
            await bot.send_message(message.from_user.id, "Вы вошли в личный кабинет", reply_markup=nav.menu_personal)


@dp.message_handler(Text(equals='Ваш профиль'))
async def profail_user(message: types.Message):
    if message.text == 'Ваш профиль':
        await bot.send_message(message.from_user.id, "Вы в своем профиле",
                               reply_markup=nav.menu_profail)


@dp.message_handler(Text(equals='Создать ТЗ'))
async def create_tz(message: types.Message):
    if message.text == 'Создать ТЗ':
        await bot.send_message(message.from_user.id, "Напишите задачу которую необходимо выполнить",
                               reply_markup=nav.menu_profail)


@dp.message_handler(Text(equals='Создать резюме'))
async def create_resume(message: types.Message):
    if message.text == 'Создать резюме':
        await bot.send_message(message.from_user.id, "Пришлите фото",
                               reply_markup=nav.menu_profail)



@dp.message_handler(Text(equals='Найти ТЗ'))
async def search_tz(message: types.Message):
    if message.text == 'Найти ТЗ':
        await bot.send_message(message.from_user.id,
                               "Введите ключевые слова поиска через запятую (python, java, django)",
                               reply_markup=nav.menu_profail)


@dp.message_handler(Text(equals='Найти резюме'))
async def search_resume(message: types.Message):
    if message.text == 'Найти резюме':
        await bot.send_message(message.from_user.id,
                               "Введите ключевые слова поиска через запятую (python, java, django)",
                               reply_markup=nav.menu_profail)


@dp.message_handler(Text(equals='🤔Полезное'))
async def polza_commands(message: types.Message):
    if message.text == '🤔Полезное':
        await bot.send_message(message.from_user.id, 'Выбери погоду и введи город',
                               reply_markup=nav.wetherMenu)


@dp.message_handler(Text(equals='🌤Погода🌤'))
async def whether_commands(message: types.Message):
    if message.text == '🌤Погода🌤':
        await bot.send_message(message.from_user.id,
                               '🌤Погода🌤',
                               reply_markup=nav.wetherMenu)
        chat_id = 459830083
        await bot.send_message(chat_id, message.from_user.username, "заходил какой то чел")


@dp.message_handler(Text(equals='🌤Узнать погоду🌤'))
async def whether_pol_commands(message: types.Message):
    if message.text == "🌤Узнать погоду🌤":
        await Form.city.set()
        await message.reply("Привет! Напиши мне название города и я пришлю сводку погоды!")
        chat_id = 459830083
        await bot.send_message(chat_id, message.from_user.username)


@dp.message_handler(Text(equals='😂Развлечения'))
async def happy_commands(message: types.Message):
    if message.text == '😂Развлечения':
        await bot.send_message(message.from_user.id, 'Генерация мата, бредовый гороскоп',
                               reply_markup=nav.otherMenu)
        chat_id = 459830083
        await bot.send_message(chat_id, message.from_user.username, "заходил какой то чел")


@dp.message_handler(Text(equals='🤬Мат'))
async def mat_commands(message: types.Message):
    if message.text == '🤬Мат':
        await bot.send_message(message.from_user.id, '🤬Мат',
                               reply_markup=nav.matMenu)
        chat_id = 459830083
        await bot.send_message(chat_id, message.from_user.username, "заходил какой то чел")


@dp.message_handler(Text(equals='👨Для парня'))
async def mat_man_commands(message: types.Message):
    if message.text == '👨Для парня':
        await message.answer(for_man())
        chat_id = 459830083
        await bot.send_message(chat_id, message.from_user.username, "заходил какой то чел")


@dp.message_handler(Text(equals='👩Для девушки'))
async def mat_woman_commands(message: types.Message):
    if message.text == '👩Для девушки':
        await message.answer(for_women())
        chat_id = 459830083
        await bot.send_message(chat_id, message.from_user.username, "заходил какой то чел")


@dp.message_handler(Text(equals='⬅ Главное меню'))
async def main_commands(message: types.Message):
    if message.text == '⬅ Главное меню':
        await bot.send_message(message.from_user.id, '⬅ Главное меню',
                               reply_markup=nav.mainMenu)


@dp.message_handler(Text(equals='⬅ Назад'))
async def main_commands(message: types.Message):
    if message.text == '⬅ Назад':
        await bot.send_message(message.from_user.id, '⬅ Назад',
                               reply_markup=nav.menu_personal)


@dp.message_handler(Text(equals='♈Гороскоп♓'))
async def gor_commands(message: types.Message):
    if message.text == '♈Гороскоп♓':
        await bot.send_message(message.from_user.id, '♈Гороскоп♓', reply_markup=nav.goroskop_menu)


@dp.message_handler(Text(equals='Получить гороскоп'))
async def main_commands(message: types.Message):
    if message.text == 'Получить гороскоп':
        await message.answer("*Выбирите свой знак зодиака*", reply_markup=nav.keyboard, parse_mode="MarkdownV2")
        # await message.reply("Введите свой знак зодиака♈♉♊♋♍♎♏♐♑♒♓♌")
        # await Form.gor.set()
        chat_id = 459830083
        await bot.send_message(chat_id, message.from_user.username, "заходил какой то чел")


@dp.callback_query_handler(Text(equals="Овен"))
async def send_random_value(call: types.CallbackQuery):
    goro = get_connect_heroku_bd(zodiac="Овен", id=index)
    await call.message.answer(goro)


@dp.callback_query_handler(Text(equals="Телец"))
async def send_random_value(call: types.CallbackQuery):
    goro = get_connect_heroku_bd(zodiac="Телец", id=index)
    await call.message.answer(goro)


@dp.callback_query_handler(Text(equals="Близнецы"))
async def send_random_value(call: types.CallbackQuery):
    goro = get_connect_heroku_bd(zodiac="Близнецы", id=index)
    await call.message.answer(goro)


@dp.callback_query_handler(Text(equals="Рак"))
async def send_random_value(call: types.CallbackQuery):
    goro = get_connect_heroku_bd(zodiac="Рак", id=index)
    await call.message.answer(goro)


@dp.callback_query_handler(Text(equals="Лев"))
async def send_random_value(call: types.CallbackQuery):
    goro = get_connect_heroku_bd(zodiac="Лев", id=index)
    await call.message.answer(goro)


@dp.callback_query_handler(Text(equals="Дева"))
async def send_random_value(call: types.CallbackQuery):
    goro = get_connect_heroku_bd(zodiac="Дева", id=index)
    await call.message.answer(goro)


@dp.callback_query_handler(Text(equals="Весы"))
async def send_random_value(call: types.CallbackQuery):
    goro = get_connect_heroku_bd(zodiac="Весы", id=index)
    await call.message.answer(goro)


@dp.callback_query_handler(Text(equals="Скорпион"))
async def send_random_value(call: types.CallbackQuery):
    goro = get_connect_heroku_bd(zodiac="Скорпион", id=index)
    await call.message.answer(goro)


@dp.callback_query_handler(Text(equals="Стрелец"))
async def send_random_value(call: types.CallbackQuery):
    goro = get_connect_heroku_bd(zodiac="Стрелец", id=index)
    await call.message.answer(goro)


@dp.callback_query_handler(Text(equals="Козерог"))
async def send_random_value(call: types.CallbackQuery):
    goro = get_connect_heroku_bd(zodiac="Козерог", id=index)
    await call.message.answer(goro)


@dp.callback_query_handler(Text(equals="Водолей"))
async def send_random_value(call: types.CallbackQuery):
    goro = get_connect_heroku_bd(zodiac="Водолей", id=index)
    await call.message.answer(goro)


@dp.callback_query_handler(Text(equals="Рыбы"))
async def send_random_value(call: types.CallbackQuery):
    goro = get_connect_heroku_bd(zodiac="Рыбы", id=index)
    await call.message.answer(goro)


@dp.message_handler(state=Form.city)
async def process_name(message: types.Message, state: FSMContext):
    if message.text == '⬅ Главное меню':
        await bot.send_message(message.from_user.id, '⬅ Главное меню',
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
            get_id(id=index)
            print('Сменил значение', str(index))
            chat_id = 459830083
            await bot.send_message(chat_id, "Сменил значение на " + str(index))
            await asyncio.sleep(3600)
        await asyncio.sleep(500)


if __name__ == '__main__':
    dp.loop.create_task(sending_messages())
    executor.start_polling(dp, skip_updates=True)
