from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class TestApp(App):
    def otevri_popup(self, button):
        popup = Popup(title='Testovací Popup', content=Button(text='Zavřít'), size_hint=(.5, .5))
        popup.open()

    def build(self):
        button = Button(text='Otevřít Popup')
        button.bind(on_press=self.show_popup)
        return button

TestApp().run()
