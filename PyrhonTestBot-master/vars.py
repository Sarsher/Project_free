import logging
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Bot, Dispatcher, executor, types
from pyowm import OWM
from pyowm.utils.config import get_default_config
guess = 0
tries = 0
upper = 101
lower = 1
from pyowm.utils import config
from pyowm.utils import timestamps
from aiogram.types import Message, Location
from textFiles import *


API_TOKEN = '5281225626:AAEKBDAWuYSsN9d0cnPLLYyhCNq1A321VbI'
Weather_api = '877510dcf66d9ccb3493fb56b6920fb5'
config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM(Weather_api, config_dict)

#Main menu buttons
lessons = KeyboardButton('📖 Уроки')
links = KeyboardButton('🔃 Полезные ссылки')
entertainment = KeyboardButton('🎯 Развлечения')
mainmenu = ReplyKeyboardMarkup(resize_keyboard=True).add(lessons).add(links).add(entertainment)

les1 = KeyboardButton('Урок №1')
les2 = KeyboardButton('Урок №2')
les3 = KeyboardButton('Урок №3')
les4 = KeyboardButton('Урок №4')
les5 = KeyboardButton('Урок №5')
les6 = KeyboardButton('Урок №6')
go_back = KeyboardButton('⬅Вернуться в Меню')
leslist = ReplyKeyboardMarkup(resize_keyboard=True).add(les6).add(les5).add(les4).add(les3).add(les2).add(les1).add(go_back)

backtomenu = ReplyKeyboardMarkup(resize_keyboard=True).add(go_back)

ent1 = KeyboardButton('Игра в кости')
ent2 = KeyboardButton('Погода на завтра')
ent3 = KeyboardButton('Бинарный поиск')
entList = ReplyKeyboardMarkup(resize_keyboard=True).add(ent1).add(ent2).add(ent3).add(go_back)

sendloc = KeyboardButton('Отправить геолокацию', request_location=True)
locationList = ReplyKeyboardMarkup(resize_keyboard=True).add(sendloc).add(go_back)

binar1 = KeyboardButton('Я хочу чтобы бот угадывал')
binar2 = KeyboardButton('Я хочу угадать число')
binarchoice = ReplyKeyboardMarkup(resize_keyboard=True).add(binar1).add(binar2)


zagadal = KeyboardButton('Я загадал')
zagadalcol = ReplyKeyboardMarkup(resize_keyboard=True).add(zagadal)

bolshe = InlineKeyboardButton('Больше⬆', callback_data = '1')
menshe = InlineKeyboardButton('Меньше⬇', callback_data = '2')
verno = InlineKeyboardButton('Верно✅', callback_data = '3')
updown = InlineKeyboardMarkup(row_width=1).add(bolshe, verno, menshe)

def userguess(a = 101, b = 1):
    global guess, upper, lower
    upper = a
    lower = b
    variants = list(i for i in range(lower, upper))
    guess = variants[round(len(variants) / 2) - 1]
    return guess

trymore = KeyboardButton('Попробовать снова')
userguessgoback = ReplyKeyboardMarkup(resize_keyboard=True).add(trymore,go_back)
