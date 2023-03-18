import sqlite3

DEFAULT_CITY = 'Yerevan'


def get_user_city(chat_id: int) -> str:
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT city FROM user_cities WHERE chat_id = (?)", (chat_id,))
    city = cursor.fetchone()
    return city[0] if city else DEFAULT_CITY


def save_user_city(chat_id: int, city: str) -> None:
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("SELECT city FROM user_cities WHERE chat_id = (?)", (chat_id,))
    result = cursor.fetchone()

    if not result:
        cursor.execute("INSERT INTO user_cities VALUES (?, ?)", (chat_id, city))
    else:
        cursor.execute("UPDATE user_cities SET city = (?) WHERE chat_id = (?)", (city, chat_id))

    connection.commit()
