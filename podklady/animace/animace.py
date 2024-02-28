from kivy.app import App
from kivy.uix.button import Button
from kivy.animation import Animation

class TestApp(App):
    def animate(self, widget):
        # Animace s odskokem
        animation = Animation(pos=(100, 100), t='out_bounce')

        # Animace s lineárním průběhem
        #animation = Animation(pos=(100, 100), t='linear')

        # Animace s kvadratickým průběhem
        #animation = Animation(pos=(20, 100), t='in_quad')

        # Animace s kubickým průběhem
        #animation = Animation(pos=(100, 100), t='in_cubic')

        # Animace s průběhem podle sinusovky
        #animation = Animation(pos=(100, 100), t='in_sine')

        # Animace s průběhem podle exponenciální funkce
        #animation = Animation(pos=(100, 100), t='in_expo')

        # Animace s průběhem podle kružnice
        #animation = Animation(pos=(100, 100), t='in_circ')

        # Animace s průběhem podle elastické funkce
        #animation = Animation(pos=(100, 100), t='in_elastic')

        # Animace s průběhem podle funkce zpomalující na konci
        #animation = Animation(pos=(100, 100), t='out_quad')

        # Animace s průběhem podle funkce zrychlující na začátku
        #animation = Animation(pos=(100, 100), t='in_out_quad')

        # Animace s průběhem podle funkce zpomalující na konci a zrychlující na začátku
        #animation = Animation(pos=(100, 100), t='in_out_cubic')

        animation.start(widget)

    def build(self):
        button = Button(text='Animuj mě')
        button.bind(on_press=self.animate)
        return button

TestApp().run()
