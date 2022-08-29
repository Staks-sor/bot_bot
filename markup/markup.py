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
goroskop_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(button_back)

# inline buttom
oven = "Овен"
telec = "Телец"
bliznec = "Близнецы"
rack = "Рак"
deva = "Дева"
vesi = "Весы"
scorpio = "Скорпион"
strelec = "Стрелец"
kozerog = "Козерог"
vodol = "Водолей"
fish = "Рыбы"
leo = "Лев"
keyboard = types.InlineKeyboardMarkup(row_width=3)
keyboard1 = types.InlineKeyboardButton(text="♈Овен", callback_data=f'bb{oven}')
keyboard2 = types.InlineKeyboardButton(text="♉Телец", callback_data=f'bb{telec}')
keyboard3 = types.InlineKeyboardButton(text="♊Близнецы", callback_data=f'bb{bliznec}')
keyboard4 = types.InlineKeyboardButton(text="♋Рак", callback_data=f'bb{rack}')
keyboard5 = types.InlineKeyboardButton(text="♍Дева", callback_data=f'bb{deva}')
keyboard6 = types.InlineKeyboardButton(text="♎Весы", callback_data=f'bb{vesi}')
keyboard7 = types.InlineKeyboardButton(text="♏Скорпион", callback_data=f'bb{scorpio}')
keyboard8 = types.InlineKeyboardButton(text="♐Стрелец", callback_data=f'bb{strelec}')
keyboard9 = types.InlineKeyboardButton(text="♑Козерог", callback_data=f'bb{kozerog}')
keyboard10 = types.InlineKeyboardButton(text="♒Водолей", callback_data=f'bb{vodol}')
keyboard11 = types.InlineKeyboardButton(text="♓Рыбы", callback_data=f'bb{fish}')
keyboard12 = types.InlineKeyboardButton(text="♌Лев", callback_data=f'bb{leo}')
keyboard.add(
    keyboard1, keyboard2,
    keyboard3, keyboard4,
    keyboard5, keyboard6,
    keyboard7, keyboard8,
    keyboard9, keyboard10,
    keyboard11, keyboard12
)

# профиль
search_vacan = 'Найти вакансию'
work_vacan = 'Работа с вакансией'
work_resume = 'работа с Резюме'
search_resume = 'Найти резюме'
button_tz = KeyboardButton(work_vacan)
button_resume = KeyboardButton(work_resume)
button_see_tz = KeyboardButton(search_vacan)
button_see_resume = KeyboardButton(search_resume)
menu_personal = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True).add(
    button_tz, button_resume,
    button_see_tz, button_see_resume,
    button_back
)

# обработка тз
create_vacant = 'Создать вакансию'
update_vacant = 'Изменить вакансию'
delete_vacant = 'Удалить вакансию'
view_vacant = 'Просмотр своей вакансии'
button_create_tz = KeyboardButton(create_vacant)
button_update = KeyboardButton(update_vacant)
button_delete = KeyboardButton(delete_vacant)
button_user_tz = KeyboardButton(view_vacant)
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
yes = "Да"
no = "Нет"
keyboard_delete = types.InlineKeyboardMarkup(row_width=2)
keyboard_delete_yes = types.InlineKeyboardButton(text="Да", callback_data=yes)
keyboard_delete_no = types.InlineKeyboardButton(text="Нет", callback_data=no)
keyboard_delete.add(
    keyboard_delete_yes, keyboard_delete_no
)


# кнопка отклика
def otclick(click):
    keyboard_otklic = types.InlineKeyboardMarkup(row_width=1)
    keyboard_otklic_i = types.InlineKeyboardButton(text="отклик", callback_data=f"cl{click}")
    keyboard_otklic.add(
        keyboard_otklic_i
    )
    return keyboard_otklic


you_already_answered = "повторный отклик"
INKB_r = types.InlineKeyboardMarkup(row_width=3, one_time_keyboard=True)
INKB_r.add(InlineKeyboardButton(text="Вы откликнулись 👌", callback_data=f"{you_already_answered}"))
