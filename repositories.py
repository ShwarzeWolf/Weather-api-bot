import sqlite3

DEFAULT_CITY = "Yerevan"
DATABASE_NAME = "database.db"


def get_user_city(chat_id):
    con = sqlite3.connect(DATABASE_NAME)
    cur = con.cursor()

    cur.execute("SELECT city FROM user_cities WHERE chat_id = (?)", (chat_id,))
    city = cur.fetchone()
    if city:
        return city[0]
    else:
        return DEFAULT_CITY


def save_user_city(chat_id, city):
    con = sqlite3.connect(DATABASE_NAME)
    cur = con.cursor()

    cur.execute("SELECT city FROM user_cities WHERE chat_id = (?)", (chat_id,))
    result = cur.fetchone()

    if not result:
        cur.execute("INSERT INTO user_cities VALUES(?, ?)", (chat_id, city))
    else:
        cur.execute("UPDATE user_cities SET city = (?) WHERE chat_id = (?)", (city, chat_id))

    con.commit()