from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Calculator(GridLayout):
    def __init__(self, **kwargs):
        super(Calculator, self).__init__(**kwargs)
        self.cols = 4 # sloupce
        self.rows = 4 # radky 

        # VYTVORENI displaye
        display = BoxLayout(orientation="vertical", size_hint_x = "3") 
        self.result = TextInput(multiline=False)
        display.add_widget(TextInput(multiline=False))
        
        self.add_widget(display)
        self.add_widget(Button(text='1', on_press=self.pridej_1)) # vytvori tlacitka, on_press funkce
        self.add_widget(Button(text='2', on_press=self.pridej_2))
        self.add_widget(Button(text='3', on_press=self.pridej_3))
        self.add_widget(Button(text='+', on_press=self.pricti))
        self.add_widget(Button(text='4', on_press=self.pridej_4))
        self.add_widget(Button(text='5', on_press=self.pridej_5))
        self.add_widget(Button(text='6', on_press=self.pridej_6))
        self.add_widget(Button(text='-', on_press=self.odecti))
        self.add_widget(Button(text='7', on_press=self.pridej_7))
        self.add_widget(Button(text='8', on_press=self.pridej_8))
        self.add_widget(Button(text='9', on_press=self.pridej_9))
        self.add_widget(Button(text='*', on_press=self.vynasob))
        self.add_widget(Button(text='/', on_press=self.vydel))
        self.add_widget(Button(text='=', on_press=self.vypocitej))
        #self.result = TextInput(multiline=False)
        #self.add_widget(self.result)

    def pridej_1(self, instance):
        self.result.text += "1"
    def pridej_2(self, instance):
        self.result.text += "2"
    def pridej_3(self, instance):
        self.result.text += "3"
    def pridej_4(self, instance):
        self.result.text += "4"
    def pridej_5(self, instance):
        self.result.text += "5"
    def pridej_6(self, instance):
        self.result.text += "6"
    def pridej_7(self, instance):
        self.result.text += "7"
    def pridej_8(self, instance):
        self.result.text += "8"
    def pridej_9(self, instance):
        self.result.text += "9"

    def pricti(self, instance):
        self.result.text += "+"
    def odecti(self, instance):
        self.result.text += "-"
    def vynasob(self, instance):
        self.result.text += "*"
    def vydel(self, instance):
        self.result.text += "/"
    def vypocitej(self, instance):
        self.result.text += "="
    
class MyApp(App):
    def build(self):
        return Calculator()


if __name__ == '__main__':
    MyApp().run()
