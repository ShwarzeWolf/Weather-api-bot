import sqlite3

connection = sqlite3.connect("database.db")

cursor = connection.cursor()
cursor.execute("""CREATE TABLE user_cities (
                chat_id INTEGER PRIMARY KEY, 
                city TEXT NOT NULL)
                """)

connection.commit()