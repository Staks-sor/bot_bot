from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_back = KeyboardButton('Главное меню')
# main menu
registraiton_buttom = KeyboardButton('Регистрация')
poleznoe_buttom = KeyboardButton('Полезное')
razvlechenia_buttom = KeyboardButton('Развлечения')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(registraiton_buttom, poleznoe_buttom, razvlechenia_buttom)

# Меню развлечения
button_goroskop = KeyboardButton('Гороскоп')
button_mat = KeyboardButton('Мат')
otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(button_goroskop, button_mat, button_back)


button_mat_man = KeyboardButton('Для парня')
button_mat_woman = KeyboardButton('Для девушки')

matMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(button_mat_man, button_mat_woman, button_back)
#Полезное меню
button_wether = KeyboardButton('Погода')
poleznoeMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(button_wether, button_back)

# wether menu
button_wet = KeyboardButton('Узнать погоду')
wetherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(button_wet, button_back)

# goroskop menu
button_gor = KeyboardButton('Получить гороскоп')
goroskop_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(button_gor, button_back)