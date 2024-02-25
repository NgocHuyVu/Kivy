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
    temp_cislo = "" #pro to abychom mohli tamto cos chtel
    rezim_barva = 0

    def smaz(self): #funkce na mazani, je tam chyba
        self.ids.vstup.text = "0"
        self.ids.vystup.text = ""
        CalculatorWidget.temp_cislo = ""

    def vymaz_jedno(self):
        self.ids.vstup.text = self.ids.vstup.text[:-1]

    def vedecka_kalkulacka(self, operace):
        vstup_cisla = self.ids.vstup.text

        if operace == "1/x" and (float(vstup_cisla) > 0 or float(vstup_cisla) < 0):
            self.ids.vstup.text = str(1 / float(vstup_cisla))

        elif operace == "x^2":
            self.ids.vstup.text = str(float(vstup_cisla) ** 2)
        
        
        elif operace == "x^3":
            self.ids.vstup.text = str(float(vstup_cisla) ** 3)

        elif operace == "√":
             self.ids.vstup.text = str(float(vstup_cisla) ** 0.5)


    def cisla(self, cislo): #funkce na cisla
        vstup_cisla = self.ids.vstup.text
        vystup_cisla = self.ids.vystup.text

        if vstup_cisla == "0":
            self.ids.vstup.text = ""
            self.ids.vstup.text += (f"{cislo}")
        else:
            self.ids.vstup.text  = (f"{vstup_cisla}{cislo}") #pridava cisla
    
    def operace(self, znak):
        znaky = ["+", "-", "*", "/", "."]
        vstup_znaku = self.ids.vstup.text
        vystup_znaku = self.ids.vystup.text

        if CalculatorWidget.temp_cislo != "":
            self.ids.vstup.text  = (f"{CalculatorWidget.temp_cislo}{znak}")
            CalculatorWidget.temp_cislo = ""
        else:
            if (len(vstup_znaku) <= 1 and vstup_znaku == "0"): #resi znamenka
                pass
            else: #zmena znamenek pri duplicitnim pouziti
                if vstup_znaku[-1] in znaky:
                    self.ids.vstup.text = vstup_znaku[:-1] + znak
                else:
                    self.ids.vstup.text  = (f"{vstup_znaku}{znak}")
    
    def vypocitej(self):
        vstup = self.ids.vstup.text
        try:
            self.ids.vystup.text = str(eval(vstup))
            self.ids.vstup.text  = self.ids.vstup.text + "="
            CalculatorWidget.temp_cislo = self.ids.vystup.text
            #print(CalculatorWidget.temp_cislo)
        except:
            self.ids.vystup.text = "Error"
            self.ids.vstup.text = "0" #automaticky to zmeni vstup na nulu

    '''
    def zmen_rezim(self, btn):
        if CalculatorWidget.rezim_barva == 0:
            btn.background_color = 0,0,0,0.5
            CalculatorWidget.rezim_barva = 1
        else:
            btn.background_color = 1,1,1,0.5
            CalculatorWidget.rezim_barva = 0
    '''
    
    def zmen_rezim(self):
        if CalculatorWidget.rezim_barva == 0:
            self.ids.rezim.background_color = 0,0,0,0.5
            CalculatorWidget.rezim_barva = 1
        else:
            self.ids.rezim.background_color = 1,1,1,0.5
            CalculatorWidget.rezim_barva = 0

    
class MyApp(App):
    def build(self):
        return CalculatorWidget()


if __name__ == '__main__':
    MyApp().run() 
