
from settings import BOT_TOKEN
from logic import get_weather

from telebot import TeleBot

bot = TeleBot(BOT_TOKEN)

default_city = 'Yerevan'
user_cities = {}


@bot.message_handler(commands=['get_weather'])
def send_weather(message):
    weather = get_weather()
    bot.send_message(message.chat.id, weather)


@bot.message_handler(commands=['setup'])
def ask_city(message):
    bot.send_message(message.chat.id, 'In what city do you live?')
    bot.register_next_step_handler(message, proceed_city)


def proceed_city(message):
    bot.send_message(message.chat.id, f'Wow, {message.text} is a great city!')
    user_cities[message.chat.id] = message.text


@bot.message_handler(commands=['get_settings'])
def get_settings(message):
    user_city = user_cities.get(message.chat.id, default_city)
    bot.send_message(message.chat.id, user_city)


bot.polling()