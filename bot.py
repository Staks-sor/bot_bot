# -*- coding: utf-8 -*-
from datetime import datetime

from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor

from bd.count_bd import *
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


class Form(StatesGroup):
    city = State()
    gor = State()
    waiting_for_tz_title = State()
    waiting_for_tz = State()
    waiting_for_tz_steck = State()
    tz_search_tz = State()



@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'Привет {message.from_user.first_name}'
                           f'! \n Я бот для поиска вакансий и работников',
                           reply_markup=nav.mainMenu)
    chat_id = 459830083
    await bot.send_message(chat_id, f"зашел {message.from_user.first_name}")


@dp.message_handler(commands=['faq'])
async def process_start_command(message: types.Message):
    await message.reply(faq)


@dp.message_handler(commands=['author'])
async def process_start_command(message: types.Message):
    await message.reply(author)


@dp.message_handler(Text(equals='Профиль'))
async def registration_commands(message: types.Message):
    if not await user_examination(message.from_user.id):
        await user_reg(message.from_user.first_name, int(message.from_user.id))
        await bot.send_message(message.from_user.id, "Автоматическая регестрация пройдена успешно")
        await bot.send_message(message.from_user.id, "Вы вошли в личный кабинет", reply_markup=nav.menu_personal)
    else:
        await bot.send_message(message.from_user.id, "Вы вошли в личный кабинет", reply_markup=nav.menu_personal)


@dp.message_handler(Text(equals=nav.work_vacan))
async def treatment_tz(message: types.Message):
    await bot.send_message(message.from_user.id, "Здесь вы можете создать изменить"
                                                 " и удалить свои технические задания",

                           reply_markup=nav.menu_tz)


@dp.message_handler(Text(equals=f"{nav.create_vacant}"))
async def create_tz(message: types.Message):
    if await tz_examination(message.from_user.id) == (0,):
        await message.answer("Название задачи")
        await Form.waiting_for_tz_title.set()
    else:
        await bot.send_message(message.from_user.id, "Вы создали макисмальное количество ТЗ")


@dp.message_handler(state=Form.waiting_for_tz_title)
async def tz_cancel(message: types.Message, state: FSMContext):
    if message.text == '⬅ Назад':
        await state.finish()
        await bot.send_message(message.from_user.id, "Вы отменили создание ТЗ и перешли в основное меню",
                               reply_markup=nav.menu_personal)

    elif message.text == 'Изменить ТЗ':
        await state.finish()
        await bot.send_message(message.from_user.id, 'Вы отменили создание ТЗ',
                               )
    elif message.text == 'Удалить ТЗ':
        await state.finish()
        await bot.send_message(message.from_user.id, 'Вы отменили создание ТЗ',
                               )
    elif message.text == 'Просмотр своих тз':
        await state.finish()
        await bot.send_message(message.from_user.id, 'Вы отменили создание ТЗ',
                               )

    else:
        await state.update_data(waiting_for_tz_title=message.text)
        await message.answer("Описание задачи")
        await Form.next()


@dp.message_handler(state=Form.waiting_for_tz)
async def tz_name(message: types.Message, state: FSMContext):
    if message.text == '⬅ Назад':
        await state.finish()
        await bot.send_message(message.from_user.id, "Вы отменили создание ТЗ и перешли в основное меню",
                               reply_markup=nav.menu_personal)

    elif message.text == 'Изменить ТЗ':
        await state.finish()
        await bot.send_message(message.from_user.id, 'Вы отменили создание ТЗ',
                               )
    elif message.text == 'Удалить ТЗ':
        await state.finish()
        await bot.send_message(message.from_user.id, 'Вы отменили создание ТЗ',
                               )
    elif message.text == 'Просмотр своих тз':
        await state.finish()
        await bot.send_message(message.from_user.id, 'Вы отменили создание ТЗ',
                               )
    else:
        await state.update_data(waiting_for_tz=message.text)
        await message.answer("Опишите технологический стек \n"
                             "Важно стек вводить через проблел."
                             "\n Пример: python java django")
        await Form.next()


@dp.message_handler(state=Form.waiting_for_tz_steck)
async def tz_create(message: types.Message, state: FSMContext):
    if message.text == '⬅ Назад':
        await state.finish()
        await bot.send_message(message.from_user.id, "Вы отменили создание ТЗ и перешли в основное меню",
                               reply_markup=nav.menu_personal)

    elif message.text == 'Изменить ТЗ':
        await state.finish()
        await bot.send_message(message.from_user.id, 'Вы отменили создание ТЗ',
                               )
    elif message.text == 'Удалить ТЗ':
        await state.finish()
        await bot.send_message(message.from_user.id, 'Вы отменили создание ТЗ',
                               )
    elif message.text == 'Просмотр своих тз':
        await state.finish()
        await bot.send_message(message.from_user.id, 'Вы отменили создание ТЗ',
                               )
    else:
        await state.update_data(waiting_for_tz_steck=message.text)
        data = await state.get_data()

        await tz_reg(data['waiting_for_tz_title'], data['waiting_for_tz'], data['waiting_for_tz_steck'],
                     int(message.from_user.id))
        await message.answer(f"{data['waiting_for_tz_title']} \n {data['waiting_for_tz']} \n "
                             f"{data['waiting_for_tz_steck']}")
        await message.answer("Вы успешно создали ТЗ!")
        await state.finish()


@dp.message_handler(Text(equals=nav.delete_vacant))
async def tz_delete(message: types.Message):
    await message.answer("Точно хотите удалить техническое задание?",
                         reply_markup=nav.keyboard_delete, parse_mode="Markdown")


@dp.callback_query_handler(Text(equals=nav.yes))
async def delete_tz(call: types.CallbackQuery):
    await call.answer(text="Успешно удалено", show_alert=True)
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.answer(await get_delete_tz(call.from_user.id))
    await call.message.answer("Успешно удалено")


@dp.callback_query_handler(Text(equals=nav.no))
async def delete_tz_no(call: types.CallbackQuery):
    await call.answer(text="Удаление отменено", show_alert=True)
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer("Удаление отменено")


@dp.message_handler(Text(equals=nav.view_vacant))
async def view_vacant(message: types.Message):
    tz = await vacant_update(message.from_user.id)
    await message.answer(f"Ваша вакансия \n *Название*\n {tz[1]} \n *что нужно сделать*\n{tz[2]} \n *Стек*\n {tz[3]}",
                         parse_mode="Markdown")


@dp.message_handler(Text(equals=nav.work_resume))
async def treatment_resume(message: types.Message):
    await bot.send_message(message.from_user.id, "Здесь вы можете создать изменить"
                                                 " и удалить свои резюме",

                           )


@dp.message_handler(Text(equals='Создать резюме'))
async def create_resume(message: types.Message):
    if await tz_examination(message.from_user.id) == (0,):
        await message.answer("Название задачи")
        await Form.waiting_for_tz_title.set()
    else:
        await bot.send_message(message.from_user.id, "Вы создали макисмальное количество ТЗ")
        await bot.send_message(message.from_user.id, "Пришлите фото, добавте описание",
                               reply_markup=nav.menu_resume)


@dp.message_handler(Text(equals=nav.search_vacan))
async def search_tz(message: types.Message):
    await bot.send_message(message.from_user.id,
                           "Введите ключевые слова поиска (python, java, django)")
    await Form.tz_search_tz.set()


@dp.message_handler(state=Form.tz_search_tz)
async def tz_create(message: types.Message, state: FSMContext):
    user_name_id = message.from_user.id
    user_name = message.from_user.first_name
    if message.text == message.text:
        tz_list = await tz_search(message.text)
        if not tz_list:
            await state.finish()
            await message.answer('Поиск не дал результатов повторите поиск, возможно вы ввели некоректные данные')
        for tz_item in tz_list:
            try:
                gg = await get_otklic(search_create=tz_item[4], search_id=user_name_id)

                if gg[0] == tz_item[4] and user_name_id:
                    await message.answer(f" *Название задачи:* \n {tz_item[1]}"
                                         f"\n *Описание задачи:* \n {tz_item[2]}"
                                         f"\n *Технологический стек:* \n {tz_item[3]}",
                                         reply_markup=nav.INKB_r, parse_mode="Markdown")
            except TypeError:
                await message.answer(f" *Название задачи:* \n {tz_item[1]}"
                                     f"\n *Описание задачи:* \n {tz_item[2]}"
                                     f"\n *Технологический стек:* \n {tz_item[3]}",
                                     reply_markup=nav.otclick(tz_item[4]), parse_mode="Markdown")

                await state.finish()
    async with state.proxy() as data:
        data['ref1'] = user_name_id
        data['ref2'] = user_name


@dp.callback_query_handler(Text(startswith='cl'))
async def search_otklic(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        user_name_id = data['ref1']
        user_name = data['ref2']
        if int(call.data[2:]) == int(user_name_id):
            await call.answer(text="Это ваше задание", show_alert=True)
        else:
            print(type(int(call.data[2:])), type(int(user_name_id)))
            await call.answer(text="Вы откликнулись", show_alert=True)
            await call.bot.edit_message_reply_markup(chat_id=call.from_user.id,
                                                     message_id=call.message.message_id, reply_markup=nav.INKB_r)

            mention = "[" + user_name + "](tg://user?id=" + str(user_name_id) + ")"
            response = f"Откликнулся, {mention}"
            await call.bot.send_message(call.data[2:], text=response,
                                        parse_mode="Markdown")
            print(call.data[2:], '<-это айди задачи(пользователя который создал) ', user_name_id)
            await otklick_create(call.data[2:], user_name_id)


@dp.callback_query_handler(Text(equals=f"{nav.you_already_answered}"))
async def already_touch(call: types.CallbackQuery):
    await call.answer(text="Вы уже откликнулись", show_alert=True)


@dp.message_handler(Text(equals=nav.search_resume))
async def search_resume(message: types.Message):
    await bot.send_message(message.from_user.id,
                           "Введите ключевые слова поиска (python, java, django)")
    await Form.tz_search_tz.set()


@dp.message_handler(Text(equals="🤔Полезное"))
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
        await bot.send_message(chat_id, f"зашел {message.from_user.username}")


@dp.message_handler(Text(equals='🌤Узнать погоду🌤'))
async def whether_pol_commands(message: types.Message):
    if message.text == "🌤Узнать погоду🌤":
        await Form.city.set()
        await message.reply("Привет! Напиши мне название города и я пришлю сводку погоды!")
        chat_id = 459830083
        await bot.send_message(chat_id, "зашел", message.from_user.username)


@dp.message_handler(Text(equals='😂Развлечения'))
async def happy_commands(message: types.Message):
    if message.text == '😂Развлечения':
        await bot.send_message(message.from_user.id, 'Генерация мата, бредовый гороскоп',
                               reply_markup=nav.otherMenu)
        chat_id = 459830083
        await bot.send_message(chat_id, f"зашел {message.from_user.username}")


@dp.message_handler(Text(equals='🤬Мат'))
async def mat_commands(message: types.Message):
    if message.text == '🤬Мат':
        await bot.send_message(message.from_user.id, '🤬Мат',
                               reply_markup=nav.matMenu)
        chat_id = 459830083
        await bot.send_message(chat_id, f"зашел {message.from_user.username}")


@dp.message_handler(Text(equals='👨Для парня'))
async def mat_man_commands(message: types.Message):
    if message.text == '👨Для парня':
        await message.answer(for_man())
        chat_id = 459830083
        await bot.send_message(chat_id, f"зашел {message.from_user.username}")


@dp.message_handler(Text(equals='👩Для девушки'))
async def mat_woman_commands(message: types.Message):
    if message.text == '👩Для девушки':
        await message.answer(for_women())
        chat_id = 459830083
        await bot.send_message(chat_id, f"зашел {message.from_user.username}")


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
    await bot.send_message(message.from_user.id, '♈Гороскоп♓', reply_markup=nav.goroskop_menu)
    await message.answer("*Выбирите свой знак зодиака*", reply_markup=nav.keyboard, parse_mode="Markdown")

    chat_id = 459830083
    await bot.send_message(chat_id, f"зашел {message.from_user.username}")


@dp.callback_query_handler(Text(startswith='bb'))
async def send_random_value(call: types.CallbackQuery):
    goro = await get_connect_heroku_bd(zodiac=call.data[2:], id=int(get_id_index()))
    await call.message.answer(f"*{call.data[2:]}* \n{goro}", parse_mode="Markdown")


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


async def sending_messages():
    index = int(get_id_index())
    print(index, "Это индекс")
    while True:
        ...
        # await asyncio.sleep(4)
        # group_id = -1001982834593
        # await bot.send_message(group_id, f"зашел {message.from_user.first_name}")
        # time_now = datetime.now()
        # print(time_now.hour)
        # if time_now.hour == 4:
        #     index += 1
        #     await get_id(id=index)
        #     print('Сменил значение', str(index))
        #     chat_id = 459830083
        #     await bot.send_message(chat_id, "Сменил значение на " + str(index))
        #     await asyncio.sleep(3600)
        # await asyncio.sleep(500)


if __name__ == '__main__':
    dp.loop.create_task(sending_messages(), )
    executor.start_polling(dp, skip_updates=True, timeout=2)
