
from settings import BOT_TOKEN
from logic import get_weather

from telebot import TeleBot

bot = TeleBot(BOT_TOKEN)

# TODO: migrate SQLite
default_city = 'Yerevan'
cities = {}


@bot.message_handler(commands=['get_weather'])
def send_weather(message):
    user_city = cities.get(message.chat.id, default_city)
    weather = get_weather(user_city)
    bot.send_message(message.chat.id, weather)


@bot.message_handler(commands=['setup'])
def ask_city(message):
    bot.send_message(message.chat.id, 'In what city do you live?')
    bot.register_next_step_handler(message, proceed_city)


def proceed_city(message):
    bot.send_message(message.chat.id, f'Wow, {message.text} is a great city!')
    cities[message.chat.id] = message.text
    bot.send_message(message.chat.id, 'I saved it to get a weather forecast')


@bot.message_handler(commands=['get_settings'])
def get_settings(message):
    user_city = cities.get(message.chat.id, default_city)
    bot.send_message(message.chat.id, f'Your city to get weather: {user_city}')


bot.polling()