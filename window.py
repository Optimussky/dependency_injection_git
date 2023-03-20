# source: https://www.youtube.com/watch?v=bXujm9PqqIU
# window.py
class Window:
    def __init__(self,storage):
        self.text = ""
        self.storage = storage

    def write_text(self,text):
        self.text += text

    def show_window(self):
        print("TextEdit")
        print(self.text)

    def save_text(self):
        self.storage.save_text(self.text)