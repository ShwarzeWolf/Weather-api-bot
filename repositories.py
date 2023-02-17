import sqlite3


default_city = 'Yerevan'


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

