# main.py
from window import Window
from textFile import TextFile
from database import Database

#storage = TextFile()
storage = Database()
w = Window(storage)
w.write_text("Greeting from Berlin.")
w.show_window()

w.save_text()