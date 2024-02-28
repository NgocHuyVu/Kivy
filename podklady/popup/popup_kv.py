from kivy.app import App
from kivy.lang import Builder
from kivy.uix.popup import Popup
import random


kv = Builder.load_file("./popup.kv")

class Priklad(App):
    def otevri_popup(self):
        for i in range(3):
            popup = Popup(title='Testovací Popup', size_hint=(random.random(),random.random()))
            popup.pos_hint = {'x': random.random(), 'y': random.random()}
            popup.open()
    
    def build(self):
        return(kv)

Priklad().run()