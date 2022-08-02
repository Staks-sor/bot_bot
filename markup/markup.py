from aiogram import types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_back = KeyboardButton('⬅ Главное меню')
button_back_Back = KeyboardButton('⬅ Назад')
# main menu
registraiton_buttom = KeyboardButton('Профиль')
poleznoe_buttom = KeyboardButton('🤔Полезное')
razvlechenia_buttom = KeyboardButton('😂Развлечения')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(registraiton_buttom, poleznoe_buttom, razvlechenia_buttom)

# Меню развлечения
button_goroskop = KeyboardButton('♈Гороскоп♓')
button_mat = KeyboardButton('🤬Мат')
otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(button_goroskop, button_mat, button_back)

button_mat_man = KeyboardButton('👨Для парня')
button_mat_woman = KeyboardButton('👩Для девушки')

matMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(button_mat_man, button_mat_woman, button_back)
# Полезное меню
button_wether = KeyboardButton('🌤Погода🌤')
poleznoeMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(button_wether, button_back)

# wether menu
button_wet = KeyboardButton('🌤Узнать погоду🌤')
wetherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(button_wet, button_back)

# goroskop menu
button_gor = KeyboardButton('Получить гороскоп')
goroskop_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(button_gor, button_back)

# inline buttom
keyboard = types.InlineKeyboardMarkup(row_width=3)
keyboard1 = types.InlineKeyboardButton(text="♈Овен", callback_data="Овен")
keyboard2 = types.InlineKeyboardButton(text="♉Телец", callback_data="Телец")
keyboard3 = types.InlineKeyboardButton(text="♊Близнецы", callback_data="Близнецы")
keyboard4 = types.InlineKeyboardButton(text="♋Рак", callback_data="Рак")
keyboard5 = types.InlineKeyboardButton(text="♍Дева", callback_data="Дева")
keyboard6 = types.InlineKeyboardButton(text="♎Весы", callback_data="Весы")
keyboard7 = types.InlineKeyboardButton(text="♏Скорпион", callback_data="Скорпион")
keyboard8 = types.InlineKeyboardButton(text="♐Стрелец", callback_data="Стрелец")
keyboard9 = types.InlineKeyboardButton(text="♑Козерог", callback_data="Козерог")
keyboard10 = types.InlineKeyboardButton(text="♒Водолей", callback_data="Водолей")
keyboard11 = types.InlineKeyboardButton(text="♓Рыбы", callback_data="Рыбы")
keyboard12 = types.InlineKeyboardButton(text="♌Лев", callback_data="Лев")
keyboard.add(
    keyboard1, keyboard2,
    keyboard3, keyboard4,
    keyboard5, keyboard6,
    keyboard7, keyboard8,
    keyboard9, keyboard10,
    keyboard11, keyboard12
)

# профиль
button_tz = KeyboardButton('Обработка ТЗ')
button_resume = KeyboardButton('Обработка Резюме')
button_see_tz = KeyboardButton('Найти ТЗ')
button_see_resume = KeyboardButton('Найти резюме')
button_ping = KeyboardButton('Отклики')
menu_personal = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True).add(
    button_tz, button_resume,
    button_see_tz, button_see_resume,
    button_ping, button_back
)

# обработка тз
crete_tz = 'Создать ТЗ'
button_create_tz = KeyboardButton(crete_tz)
button_update = KeyboardButton('Изменить ТЗ')
button_delete = KeyboardButton('Удалить ТЗ')
button_user_tz = KeyboardButton('Просмотр своих тз')
menu_tz = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True).add(
    button_create_tz,
    button_update,
    button_delete,
    button_user_tz,
    button_back_Back
)
# обработка резюме

button_create_resume = KeyboardButton('Создать Резюме')
button_update_resume = KeyboardButton('Изменить Резюме')
button_delete_resume = KeyboardButton('Удалить Резюме')
button_user_resume = KeyboardButton('Просмотр своих Резюме')
menu_resume = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True).add(
    button_create_resume,
    button_update_resume,
    button_delete_resume,
    button_user_resume,
    button_back_Back
)
# удаление технического задания
keyboard_delete = types.InlineKeyboardMarkup(row_width=2)
keyboard_delete_yes = types.InlineKeyboardButton(text="Да", callback_data="Да")
keyboard_delete_no = types.InlineKeyboardButton(text="Нет", callback_data="Нет")
keyboard_delete.add(
    keyboard_delete_yes, keyboard_delete_no
)

# кнопка отклика
keyboard_otklic = types.InlineKeyboardMarkup(row_width=2)
keyboard_otklic_i = types.InlineKeyboardButton(text="Откликнуться", callback_data="отклик")
keyboard_otklic.add(
    keyboard_otklic_i
)
