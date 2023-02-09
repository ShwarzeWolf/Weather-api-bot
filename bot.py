
from settings import BOT_TOKEN
from logic import get_weather

from telebot import TeleBot

bot = TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['get_weather'])
def send_weather(message):
    weather = get_weather()
    bot.send_message(message.chat.id, weather)


bot.polling()