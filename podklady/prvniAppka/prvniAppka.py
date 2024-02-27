from kivy.app import App
from kivy.uix.label import Label
from kivy.lang.builder import Builder

#kv = Builder.load_file("./prvniAppka.kv")

class Priklad(App):
    def build(self):
        return Label(text='hi mom', color=(1,0,0))
        #return(kv)

Priklad().run()
