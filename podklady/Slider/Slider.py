from kivy.app import App
from kivy.uix.slider import Slider
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang.builder import Builder

kv = Builder.load_file("./Slider.kv")

'''
class Priklad(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")
        slider = Slider(min=0, max=100, value=50)
        text = Label(text=str(slider.value))

        def hodnota_slider(instance, value):
            text.text = str(value)

        slider.bind(value=hodnota_slider)
        layout.add_widget(text)
        layout.add_widget(slider)
        return layout
'''
class Priklad(App):
    def build(self):
        return kv

Priklad().run()
