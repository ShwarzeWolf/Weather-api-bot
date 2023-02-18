import sqlite3

con = sqlite3.connect("database.db")

cur = con.cursor()

cur.execute("""CREATE TABLE user_cities (chat_id INTEGER PRIMARY KEY, city TEXT NOT NULL)""")

con.commit()