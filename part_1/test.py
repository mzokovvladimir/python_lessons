import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = 'YOUR_TOKEN'
OPENWEATHER_API = ''

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + OPENWEATHER_API + "&q=" + city
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"] - 273.15  # Кельвины в Цельсии
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        return f"В городе {city} сейчас: \nТемпература: {current_temperature:.2f} °C\nДавление: {current_pressure} hPa\nВлажность: {current_humidiy}%\nОписание: {weather_description}"
    else:
        return "Город не найден."


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button = KeyboardButton("Узнать погоду")
    markup.add(button)
    await message.reply("Привет! Чтобы узнать погоду, нажмите кнопку.", reply_markup=markup)


@dp.message_handler(text='Узнать погоду')
async def weather(message: types.Message):
    await message.reply("В каком городе вы хотите узнать погоду?")


@dp.message_handler()
async def echo(message: types.Message):
    city = message.text
    weather_data = await get_weather(city)
    await message.answer(weather_data)


if __name__ == '__main__':
    asyncio.run(executor.start_polling(dp, skip_updates=True))
