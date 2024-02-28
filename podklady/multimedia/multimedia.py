from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
from kivy.uix.video import Video
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.progressbar import ProgressBar
from kivy.uix.gridlayout import GridLayout

class Priklad(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")
        zvuk = SoundLoader.load('bird.mp3')
        obrazek = Image(source="pan.jpg")
        delka = Label(text=str(zvuk.length))
        posuvnik = Slider(min=0, max=zvuk.length, value=zvuk.get_pos())
        progress_bar = ProgressBar()
        progress_bar.min = 0
        progress_bar.max = zvuk.length
        progress_bar.value = int(zvuk.get_pos())
        button_on = Button(text="on", background_color=(0,1,0,1))
        button_off = Button(text="off", background_color=(0,0.5,1))
        layout.add_widget(obrazek)
        layout.add_widget(delka)
        #layout.add_widget(posuvnik)
        layout.add_widget(progress_bar)
        layout.add_widget(button_on)
        layout.add_widget(button_off)
        def aktualizuj_pozici(instance, value):
            zvuk.seek(value)

        posuvnik.bind(value=aktualizuj_pozici)
        layout.add_widget(posuvnik)
        #delka.bind(text=zvuk.lenght)
        #if zvuk:
        #    print(f"Délka zvuku: {zvuk.length}")
        #    zvuk.play()
        #return Label(text='Hello world')
        #return Image(source='pan.jpg')
        return layout

#class Priklad(App):
#    def build(self):
#        return Video(source="dog.mp4")

Priklad().run()
'''
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
from kivy.uix.video import Video

class Priklad(App):
    def build(self):
        #return Image(source='pan.jpg')
        zvuk = SoundLoader.load('bird.mp3')
        if zvuk:
            print(f"Délka zvuku: {zvuk.length}")
            zvuk.play()
        #return Label(text='Hello world')
        return Image(source='pan.jpg')

#class Priklad(App):
#    def build(self):
#        return Video(source="dog.mp4")

Priklad().run()
'''