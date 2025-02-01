from time import gmtime, strftime
import sqlite3

class Note:
    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.time_stamp = strftime("%H:%M:%S %Y-%m-%d", gmtime())
        DBManager('notes_db').add(self)

    def edit_title(self, title):
        self.title = title

    def edit_text(self, text):
        self.text = text



    def __str__(self):
        return f"{self.title}:\n\t{self.text}\n\n{self.time_stamp}"
    
#notes
#title text time



class DBManager:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.c = self.conn.cursor()
        
    def add(self, note):
        title = note.title
        text = note.text
        time = note.time_stamp
        with self.conn:
            self.c.execute(f"INSERT INTO Notes VALUES ('{title}', '{text}', '{time}')")

    def remove(self):
        pass

    def edit(self):
        pass

    def get(self):
        pass

# Note('Barca vs Alaves Preditions', 'Barca got the chance to close down on madrid if they win')
conn = sqlite3.connect('notes_db')
c = conn.cursor()
c.execute(f"SELECT * FROM Notes")
for headline in c.fetchall():
    print(headline)