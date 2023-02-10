
from logic import get_weather

from telebot import TeleBot
from settings import BOT_TOKEN

bot = TeleBot(BOT_TOKEN)
city = 'Yerevan'

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
    global city
    city = message.text
    bot.send_message(message.chat.id, 'I saved it in settings')


@bot.message_handler(commands=['get_settings'])
def get_city(message):
    bot.send_message(message.chat.id, f'Your current city is {city}')


bot.polling()