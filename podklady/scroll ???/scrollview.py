from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        for i in range(30):
            btn = Button(text=str(i), size_hint_y=None, height=40)
            layout.add_widget(btn)
        scroll_view = ScrollView()
        scroll_view.add_widget(layout)
        return scroll_view

TestApp().run()
