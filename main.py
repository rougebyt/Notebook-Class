from time import gmtime, strftime


class Note:
    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.time_stamp = strftime("%H:%M:%S %Y-%m-%d", gmtime())


    def edit_title(self, title):
        self.title = title

    def edit_text(self, text):
        self.text = text



    def __str__(self):
        return f"{self.title}:\n\t{self.text}\n\n{self.time_stamp}"
    



