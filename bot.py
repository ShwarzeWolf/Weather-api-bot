
from settings import BOT_TOKEN
from logic import get_weather

from telebot import TeleBot
import sqlite3
bot = TeleBot(BOT_TOKEN)

# TODO: migrate SQLite
default_city = 'Yerevan'
cities = {}
# chat_id : city_name | 224787: Surgut


def get_user_city(chat_id):
    con = sqlite3.connect("database.db")
    cur = con.cursor()

    cur.execute("SELECT city FROM user_cities WHERE chat_id = (?)", (chat_id,))
    city = cur.fetchone()
    if city:
        return city[0]
    else:
        return default_city


def save_user_city(chat_id, city):
    con = sqlite3.connect("database.db")
    cur = con.cursor()

    cur.execute("SELECT city FROM user_cities WHERE chat_id = (?)", (chat_id,))
    result = cur.fetchone()

    if not result:
        cur.execute("INSERT INTO user_cities VALUES(?, ?)", (chat_id, city))
    else:
        cur.execute("UPDATE user_cities SET city = (?) WHERE chat_id = (?)", (city, chat_id))

    con.commit()


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