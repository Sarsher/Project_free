import logging
import string

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, executor, types
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from aiogram.types import Message, Location
from pprint import pprint
import requests
from pyowm.utils.config import get_default_config
import pyowm
from vars import *
from textFiles import *
from Kosti import *


long = 0
latd = 0
mgr = owm.weather_manager()
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

#                           start and intro
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer(intro, reply_markup=mainmenu)


#                           list of lessons
@dp.message_handler(text = '📖 Уроки')
async def mainMenu(message: types.Message):
    await message.answer('Выберите урок', reply_markup=leslist)


#                           useful links list
@dp.message_handler(text = '🔃 Полезные ссылки')
async def usefullinkslist(message: types.Message):
    await message.answer(usefulLinks, reply_markup=backtomenu)
    if '⬅Вернуться в Меню' in message.text:
        await message.answer(intro, reply_markup=mainmenu)


#                           entertainment
@dp.message_handler(text = '🎯 Развлечения')
async def entertainment(message: types.Message):
    await message.answer('Куда пойдем?', reply_markup=entList)


#                           Weather Forecast
@dp.message_handler(text = 'Погода на завтра')
async def geolocation (message: types.Message):
    await message.answer('Отправьте нам геолокацию', reply_markup=locationList)

@dp.message_handler(content_types=['location'])
async def locationwork (message: types.Message):
    if message.location is not None:
        a = dict(message.location)
        global lat, lon
        latd = a['latitude']
        long = a['longitude']
        observation = mgr.weather_at_place('Tashkent,uz')
        w = observation.weather
        await message.answer(f'''
Погода в вашем регионе: {w.detailed_status}. 
Температура: {round(w.temperature('celsius')['temp'])}°C.''', reply_markup= backtomenu)


#                           Binar search
@dp.message_handler(text = 'Бинарный поиск')
async def binarchoicemenu (message: types.Message):
    await message.answer('Выберите игру\n'
                         '1. Вы загадываете число и бот угадывает\n'
                         '2. Бот загадывает число и вы угадываете', reply_markup= binarchoice)



#                           PCguess
@dp.message_handler(text = 'Я хочу чтобы бот угадывал')
async def bingame1 (message: types.Message):
    await message.answer('И так начнем. Для начала выберите число от 1 до 100', reply_markup=zagadalcol)


@dp.message_handler(text = 'Я загадал')
async def bingame1start (message: types.Message):
    global guess
    guess = userguess()
    await message.answer(f'Ваше число {guess}?', reply_markup=updown)


@dp.callback_query_handler(text="1")
async def ifmore (call: types.CallbackQuery):
    global guess
    guess = userguess(a = upper, b = guess)
    await call.message.answer(f'Ваше число {guess}?', reply_markup=updown)

@dp.callback_query_handler(text="2")
async def ifless (call: types.CallbackQuery):
    global guess
    guess = userguess(a = guess, b = lower)
    await call.message.answer(f'Ваше число {guess}?', reply_markup=updown)
@dp.callback_query_handler(text="3")
async def ifless (call: types.CallbackQuery):
    await call.message.answer(f'Ваше число {guess} - угаданно.', reply_markup=userguessgoback)

@dp.message_handler(text = 'Попробовать снова')
async def binarchoicemenu (message: types.Message):
    await message.answer('Выберите игру\n'
                         '1. Вы загадываете число и бот угадывает\n'
                         '2. Бот загадывает число и вы угадываете', reply_markup= binarchoice)









#                                   user guess
@dp.message_handler(text='Я хочу угадать число')
async def bingame2(message: types.Message):
    await message.answer()
























#                           lessons content
@dp.message_handler()
async def listOfLesson(message: types.Message):
    if 'Урок №1' in message.text:
        await message.answer(theme1)
    elif 'Урок №2' in message.text:
        await message.answer(theme2)
    elif 'Урок №3' in message.text:
        await message.answer(theme3)
    elif 'Урок №4' in message.text:
        await message.answer(theme4)
    elif 'Урок №5' in message.text:
        await message.answer(theme5)
    elif 'Урок №6' in message.text:
        await message.answer(theme6)
    elif '⬅Вернуться в Меню' in message.text:
        await message.answer(intro, reply_markup=mainmenu)
    while message.text == 'Игра в кости':
        await message.answer('И так ваши кости:')
        result1, result2 = kostigame()
        finalResult = (f'{result1}               {result2}')
        await message.answer(finalResult)
        break





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

