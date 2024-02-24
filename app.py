from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.lang.builder import Builder

Builder.load_file("./my.kv") #loadnes file z root slozky
Window.size = (350, 600) #velikost okna, sirka/vyska

class CalculatorWidget(Widget):
    def smaz(self): #funkce na mazani, je tam chyba
        self.ids.vstup.text = "0"

    def tlacitka_cisla(self, cislo): #funkce na cisla
        vstup_cisla = self.ids.vstup.text

        if vstup_cisla == "0":
            self.ids.vstup.text = ""
            self.ids.vstup.text += (f"{cislo}")

    '''
    TOHLE je teoreticky funkcni, jen staci loadnout vstup na sledovani

    def operatory_duplicita(self, button):
        text = button.text
        vstup = self.ids.vstup.text
        self.vstup = TextInput()
        if text.isdigit():
            vstup.text += text
            self.check_char = text
        elif text in self.operatory:
            if self.check_char not in self.operatory:
                self.vstup.text += f" {text} "
                self.check_char = text
    '''


    
class MyApp(App):
    def build(self):
        return CalculatorWidget()


if __name__ == '__main__':
    MyApp().run() #my.kv se spousti podle tridy MyApp, neco jako C# oddeli velky pismena jako slovo
