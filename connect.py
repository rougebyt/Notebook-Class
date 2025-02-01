import sqlite3

conn = sqlite3.connect("notes_db")
c = conn.cursor()

c.execute("""CREATE TABLE Notes (
          id integer primary key,
          Title text,
          Text text,
          time_stamp text
          )""")

