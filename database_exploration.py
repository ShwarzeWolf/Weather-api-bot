import sqlite3
con = sqlite3.connect("tutorial.db")

cursor = con.cursor()
# cursor.execute("CREATE TABLE movie(title, year, score)")
#
# res = cursor.execute("SELECT name FROM sqlite_master")
# print(res.fetchone())
#
# res = cursor.execute("SELECT * FROM movie")
# print(res.fetchone())
#
# cursor.execute("""
#     INSERT INTO movie VALUES
#         ('Monty Python and the Holy Grail', 1975, 8.2),
#         ('And Now for Something Completely Different', 1971, 7.5)
# """)
#
# con.commit()
#
# res = cursor.execute("SELECT * FROM movie")
# print(res.fetchall())

data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]
cursor.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
con.commit()  # Remember to commit the transaction after executing INSERT.


res = cursor.execute("SELECT * FROM movie")
print(res.fetchall())