from kivy.app import App
from kivy.uix.label import Label

class Priklad(App):
    def build(self):
        return Label(text='hi mom', color=(1,0,0))

Priklad().run()
