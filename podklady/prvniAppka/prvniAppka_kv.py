from kivy.app import App
from kivy.uix.label import Label
from kivy.lang.builder import Builder

kv = Builder.load_file("./prvniAppka.kv")

class Priklad(App):
    def build(self):
        return(kv)

Priklad().run()
