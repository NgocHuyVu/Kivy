from kivy.app import App
from kivy.uix.image import Image

class Priklad(App):
    def build(self):
        return Image(source='pan.jpg')

Priklad().run()
