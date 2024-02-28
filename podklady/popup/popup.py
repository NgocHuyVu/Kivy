from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import random

class Priklad(App):
    def otevri_popup(self, button):
        for i in range(3):
            popup = Popup(title='Testovací Popup', content=Button(text='Zavřít'), size_hint=(random.random(),random.random()))
            zavri_popup = Button(text='Zavřít')
            zavri_popup.bind(on_release=popup.dismiss)  # Přidáno
            popup.content = zavri_popup
            popup.pos_hint = {'x': random.random(), 'y': random.random()}
            popup.open()

    def build(self):
        button = Button(text='Otevři popup')
        button.bind(on_press=self.otevri_popup)
        return button

Priklad().run()
