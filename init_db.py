import sqlite3

connection = sqlite3.connect("database.db")

cursor = connection.cursor()

with open("schema.sql") as init_script:
    cursor.executescript(init_script.read())

connection.commit()