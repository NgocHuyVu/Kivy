import kivy 
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp

dropdown = DropDown()
options = ["Muž", "Žena", "Jiné"] 
for option in options:
    btn = Button(text=option, size_hint_y=None, height=40)
    btn.bind(on_release=lambda btn: dropdown.select(btn.text))
    dropdown.add_widget(btn)
mainbutton = Button(text ='Pohlaví', size_hint =(None, None), pos =(600, 300))
mainbutton.bind(on_release = dropdown.open)
dropdown.bind(on_select = lambda instance, x: setattr(mainbutton, 'text', x))
runTouchApp(mainbutton)