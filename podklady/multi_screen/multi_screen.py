from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class ManagerScreen(ScreenManager):
    pass

kv = Builder.load_file("./multi_screen.kv")

class Priklad(App):
    def build(self):
        return kv

if __name__ == '__main__':
    Priklad().run()