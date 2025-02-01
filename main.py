from datetime import datetime


from time import gmtime, strftime





class Note:
    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.time_stamp = strftime("%H:%M:%S %Y-%m-%d", gmtime())
    def __str__(self):
        return f"{self.title}:\n\t{self.text}\n\n{self.time_stamp}"
    



class Edit():
    def __init__(self, Note):
        
        self.note = Note
        self.note.time_stamp = strftime("%H:%M:%S %Y-%m-%d", gmtime())
    def edit_title(self, title):
        self.note.title = title

    def edit_text(self, text):
        self.note.text = text



n1 = Note("Real-Espanol", "Madrid drew against Espanol in the first Half....")
print(n1)


Edit(n1).edit_title("Fuck Madrid")
Edit(n1).edit_text('VADRID GOT FUCKED BY EXPANOL')
print()
print()
print(n1)



# import 