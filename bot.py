
from settings import BOT_TOKEN
from logic import get_weather

from telebot import TeleBot

bot = TeleBot(BOT_TOKEN)

# TODO: migrate SQLite
default_city = 'Yerevan'
cities = {}

import sqlite3


def get_user_city(chat_id):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT city FROM user_cities where user_id = (?)", (chat_id,))
    city = cursor.fetchone()
    return city[0] if city else default_city


def save_user_city(chat_id, city):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute("SELECT city FROM user_cities where user_id = (?)", (chat_id,))
    result = cursor.fetchone()

    if not result:
        cursor.execute("INSERT INTO user_cities VALUES(?, ?)", (chat_id, city))
    else:
        cursor.execute("UPDATE user_cities SET city = (?) WHERE user_id = (?)", (city, chat_id))
    connection.commit()


@bot.message_handler(commands=['get_weather'])
def send_weather(message):
    user_city = get_user_city(message.chat.id)
    weather = get_weather(user_city)
    bot.send_message(message.chat.id, weather)


@bot.message_handler(commands=['setup'])
def ask_city(message):
    bot.send_message(message.chat.id, 'In what city do you live?')
    bot.register_next_step_handler(message, proceed_city)


def proceed_city(message):
    bot.send_message(message.chat.id, f'Wow, {message.text} is a great city!')
    save_user_city(message.chat.id, message.text)
    bot.send_message(message.chat.id, 'I saved it to get a weather forecast')


@bot.message_handler(commands=['get_settings'])
def get_settings(message):
    user_city = get_user_city(message.chat.id)
    bot.send_message(message.chat.id, f'Your city to get weather: {user_city}')


bot.polling()