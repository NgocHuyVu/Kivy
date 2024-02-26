from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import NoTransition
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.clock import Clock
import math
from random import randint

#Builder.load_file("./my.kv") #loadnes file z root slozky
Window.size = (350, 600) #velikost okna, sirka/vyska

#Přepsal jsem z widget na Screen
class CalculatorWidget(Screen):
    temp_cislo = "" #pro to abychom mohli tamto cos chtel

    def smaz(self): #funkce na mazani, je tam chyba
        self.ids.vstup.text = "0"
        self.ids.vystup.text = ""
        CalculatorWidget.temp_cislo = ""

    def vymaz_jedno(self):
        if len(self.ids.vstup.text) > 1:
            self.ids.vstup.text = self.ids.vstup.text[:-1]
        else:
            self.ids.vstup.text = "0"


    def cisla(self, cislo): #funkce na cisla
        vstup_cisla = self.ids.vstup.text
        vystup_cisla = self.ids.vystup.text

        if vstup_cisla == "0":
            self.ids.vstup.text = ""
            self.ids.vstup.text += (f"{cislo}")
        elif vstup_cisla == "PI":
            self.ids.vstup.text = str(math.pi)
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
    
    def zmen_rezim(self):
        for button_id in self.ids.keys():
            button = self.ids[button_id]
            if isinstance(button, Button):
                if button.background_color == [0, 1, 1, 1]:
                    button.background_color = [0.7, 0.7, 0.7, 1]
                else:
                    button.background_color = [0, 1, 1, 1]
    
    def vedecka_kalkulacka_velikost(self):
        Window.size = (700,400)

class ScienceCalculatorWidget(Screen):
    temp_cislo = "" #pro to abychom mohli tamto cos chtel

    def smaz(self):
        self.ids.vstup.text = "0"
        self.ids.vystup.text = ""
        CalculatorWidget.temp_cislo = ""

    def vymaz_jedno(self):
        if len(self.ids.vstup.text) > 1:
            self.ids.vstup.text = self.ids.vstup.text[:-1]
        else:
            self.ids.vstup.text = "0"

    def vedecka_kalkulacka(self, operace):
        vstup_cisla = self.ids.vstup.text

        if operace == "1/x" and (float(vstup_cisla) > 0 or float(vstup_cisla) < 0):
            self.ids.vstup.text = str(1 / float(vstup_cisla))

        elif operace == "x^2":
            self.ids.vstup.text = str(float(vstup_cisla) ** 2)

        elif operace == "x^3":
            self.ids.vstup.text = str(float(vstup_cisla) ** 3)

        elif operace == "√" and (float(vstup_cisla) >= 0):
            self.ids.vstup.text = str(float(vstup_cisla) ** 0.5)

        elif operace == "10^x":
            self.ids.vstup.text = str(10 ** float(vstup_cisla))

        elif operace == "log" and (float(vstup_cisla) >= 0):
            self.ids.vstup.text = str(math.log10(float(vstup_cisla)))
            
        elif operace == "ln" and (float(vstup_cisla) >= 0):
            self.ids.vstup.text = str(math.log(float(vstup_cisla)))


    def cisla(self, cislo): #funkce na cisla
        vstup_cisla = self.ids.vstup.text
        vystup_cisla = self.ids.vystup.text

        if vstup_cisla == "0":
            self.ids.vstup.text = ""
            self.ids.vstup.text += (f"{cislo}")
        elif vstup_cisla == "PI":
            self.ids.vstup.text = str(math.pi)
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
    
    def zmen_rezim(self):
        for button_id in self.ids.keys():
            button = self.ids[button_id]
            if isinstance(button, Button):
                if button.background_color == [0, 1, 1, 1]:
                    button.background_color = [0.7, 0.7, 0.7, 1]
                else:
                    button.background_color = [0, 1, 1, 1]
    
    def vedecka_kalkulacka_velikost(self):
        Window.size = (350,600)


class SnakeHlava(Widget):
    def __init__(self, pos):
        super().__init__(pos=pos)
        self.size = (50, 50)
        with self.canvas:
            self.rect = Rectangle(pos=self.pos, size=self.size)

    def pohyb(self, dx, dy):
        self.pos = [self.pos[0] + dx, self.pos[1] + dy]
        self.rect.pos = self.pos

class Jidlo(Widget):
    def __init__(self, pos):
        super().__init__(pos=pos)
        self.size = (50, 50)
        with self.canvas:
            Color(1,0,0)
            self.rect = Rectangle(pos=self.pos, size=self.size)
    
    def premisti(self):
        #self.pos = [randint(0, Window.width - 50), randint(0, Window.height - 50)]
        #self.pos = [randint(0, 650), randint(2100,2250)]
        self.pos = [randint(0, 650), randint(1000,1170)]
        self.rect.pos = self.pos

class SnakeCalculator(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.snake = SnakeHlava((300, 1100))
        self.jidlo = Jidlo(self.nahodnaLokace())
        self.add_widget(self.snake)
        self.add_widget(self.jidlo)
        self.smer = 'doprava'
        Clock.schedule_interval(self.pohyb_kont, 1)

    #def pohyb_kont(self, dt):
    #    self.snake.pohyb(dt, 0)

    def pohyb_kont(self, dt):
        dx = 0
        dy = 1100
        if self.smer == 'nahoru':
            self.snake.pohyb(0, 50)
        elif self.smer == 'dolu':
            self.snake.pohyb(0, -50)
        elif self.smer == 'doleva':
            self.snake.pohyb(-50, 0)
        elif self.smer == 'doprava':
            self.snake.pohyb(50, 0)

        novy_x = self.snake.pos[0] + dx
        novy_y = self.snake.pos[1] + dy
        #print(novy_x)
        #print(novy_y)
        print(novy_x, novy_y) #0-650 sirka
        #print(novy_y) #2100-2250 vyska
        print(f"Pozice jídla: {self.pos}")
        if novy_x > 650:
            self.snake.pohyb(-50, 0)
        elif novy_x < 0:
            self.snake.pohyb(50, 0)
        elif novy_y > 2250:
            self.snake.pohyb(0,-50)
        elif novy_y < 2100:
            self.snake.pohyb(0,50)

        if self.snake.collide_widget(self.jidlo): #tohle predelat
            self.jidlo.premisti()
        

    def pohyb_nahoru(self, instance):
        self.smer = 'nahoru'

    def pohyb_dolu(self, instance):
        self.smer = 'dolu'

    def pohyb_vlevo(self, instance):
        self.smer = 'doleva'

    def pohyb_vpravo(self, instance):
        self.smer = 'doprava'

    def nahodnaLokace(self):
        return [randint(0, 650), randint(2100,2250)]


class CalculatorManager(ScreenManager):
    pass

kv = Builder.load_file("./my.kv")

class MyApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    MyApp().run() 
