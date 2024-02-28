from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window

class MyWidget(Widget):
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
        
        with self.canvas:
            self.canvas.before.clear()
            self.canvas.before.add(Color(1, 0, 0, 1)) 
            
            # Výpočet pozice čtverce na základě velikosti obrazovky
            width, height = Window.size
            size = (200, 100)
            pos = ((width - size[0]) / 2, (height - size[1]) / 2)
            self.rect = Rectangle(pos=pos, size=size)

    def update_rectangle(self, pos, size):
        self.rect.pos = pos
        self.rect.size = size


class MyApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    MyApp().run()

# Canvas je grafický kontejner, do kterého můžeme kreslit různé prvky např. čáry, obdélníky, čtverce, elipsy a další.