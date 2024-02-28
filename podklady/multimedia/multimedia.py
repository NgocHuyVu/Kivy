from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader

class Priklad(App):
    def build(self):
        self.zvuk = SoundLoader.load('bird.mp3')
        if self.zvuk:
            print(f"Délka zvuku: {self.zvuk.length}")

        layout = BoxLayout(orientation='vertical')

        layout.add_widget(Image(source='pan.jpg'))

        button_layout = BoxLayout(orientation='horizontal')
        play_button = Button(text='Spusť')
        play_button.bind(on_press=self.play_sound)
        button_layout.add_widget(play_button)

        stop_button = Button(text='Zastav')
        stop_button.bind(on_press=self.stop_sound)
        button_layout.add_widget(stop_button)

        layout.add_widget(button_layout)

        return layout

    def play_sound(self, instance):
        self.zvuk.play()

    def stop_sound(self, instance):
        self.zvuk.stop()

Priklad().run()
