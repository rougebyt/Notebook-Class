from time import gmtime, strftime
import sqlite3

class Note:
    def __init__(self, id, title, text):
        self.id = id
        self.title = title
        self.text = text
        self.time_stamp = strftime("%H:%M:%S %Y-%m-%d", gmtime())
        
    def save(self):
        DBManager('notes_db', self).add()

    def edit_title(self, title):
        self.title = title

    def edit_text(self, text):
        self.text = text


    def __str__(self):
        return f"{self.title}:\n\t{self.text}\n\n{self.time_stamp}"
    

class DBManager:
    def __init__(self, db='notes_db', note=None):
        self.conn = sqlite3.connect(db)
        self.c = self.conn.cursor()
        self.note = note
      
    def add(self):
        with self.conn:
            # self.c.execute(f"INSERT INTO Notes VALUES ({self.note.id},'{self.note.title}', '{self.note.text}', '{self.note.time_stamp}')")
            self.c.execute("INSERT INTO Notes VALUES (?, ?, ?, ?)", 
                           (self.note.id, self.note.title, self.note.text, self.note.time_stamp))

    def remove(self,id):
        with self.conn:
            # self.c.execute("DELETE FROM Notes WHERE id=?", (id))
            self.c.execute("DELETE FROM Notes WHERE id=?", (id,))

    def edit(self):
        pass

    def get(self):
        self.c.execute(f"SELECT * FROM Notes")
        return self.c.fetchall()
    
DBManager().remove(1)

# Note(10, "Aymil Amjad", "Jaja askdfjlaskdjfk").save()
# print(DBManager().get())