from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader

class Priklad(App):
    def build(self):
        #return Image(source='pan.jpg')
        zvuk = SoundLoader.load('bird.mp3')
        if zvuk:
            print(f"Délka zvuku: {zvuk.length}")
            zvuk.play()
        #return Label(text='Hello world')
        return Image(source='pan.jpg')

Priklad().run()
