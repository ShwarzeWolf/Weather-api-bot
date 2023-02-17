import sqlite3

connection = sqlite3.connect('database.db')

cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS user_cities (
                  user_id INTEGER PRIMARY KEY,
                  city TEXT NOT NULL);
                  """)