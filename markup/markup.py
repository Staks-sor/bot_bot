from aiogram import types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_back = KeyboardButton('⬅ Главное меню')
# main menu
registraiton_buttom = KeyboardButton('Войти')
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
#Полезное меню
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
keyboard.add(keyboard1, keyboard2, keyboard3, keyboard4, keyboard5, keyboard6, keyboard7,
             keyboard8, keyboard9, keyboard10, keyboard11, keyboard12)


#личный кабинет
button_profail = KeyboardButton('Ваши профиль')
button_tz = KeyboardButton('Создать ТЗ')
button_resume = KeyboardButton('Создать резюме')
button_see_tz = KeyboardButton('Найти ТЗ')
button_see_resume = KeyboardButton('Поиск резюме')
menu_personal = ReplyKeyboardMarkup(resize_keyboard=True).add(button_profail, button_tz, button_resume,
                                                              button_tz, button_resume, button_back)

