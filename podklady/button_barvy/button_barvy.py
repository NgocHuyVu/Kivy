from kivy.app import App
from kivy.uix.button import Button
import random
from kivy.lang.builder import Builder

#kv = Builder.load_file("./button_barvy.kv")


class Priklad(App):
    def build(self):
        self.button = Button(text='Stiskni mě', background_color = (1,1,1,1))
        self.button.bind(on_press=self.klik)
        return self.button

    def klik(self, instance):
        self.button.background_color = (random.random(),random.random(),random.random(),1)
'''
class Priklad(App):
    def build(self):
        return kv

    def klik(self):
        return (random.random(),random.random(),random.random(),1)
'''
Priklad().run()
