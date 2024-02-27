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
#from kivy.config import Config
from kivy.utils import platform
import math
from random import randint


#Config.set('graphics', 'width', '1920')
#Config.set('graphics', 'height', '1080')
#Builder.load_file("./my.kv") #loadnes file z root slozky
#Window.size = (350, 600) #velikost okna, sirka/vyska
#Config.set('graphics', 'resizable', False)
#Config.set('graphics', 'width', '350')
#Config.set('graphics', 'height', '600')

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

class SnakeTelo(Widget):
    def __init__(self, pos):
        super().__init__(pos=pos)
        self.size = (50, 50)
        with self.canvas:
            self.rect = Rectangle(pos=self.pos, size=self.size)

class Jidlo(Widget):
    def __init__(self, pos):
        super().__init__(pos=pos)
        self.size = (50, 50)
        with self.canvas:
            Color(1,0,0)
            self.rect = Rectangle(pos=self.pos, size=self.size)
    
    def premisti(self):
        #self.pos = [randint(0, Window.width - 50), randint(0, Window.height - 50)]
        #self.pos = [randint(0, 650), randint(2100,2250)] 1175
        #self.pos = [randint(0, 650), randint(1000,1170)]
        #self.pos = [randint(0, 650), randint(1000,1170)]
        self.pos = [randint(0, 13) * 50, randint(20,23) * 50]
        #self.pos = [randint(0, 13) * 50, randint(200,204) * 50]
        self.rect.pos = self.pos

class SnakeCalculator(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.snake = [SnakeHlava((300, 1100))]
        self.jidlo = Jidlo(self.nahodnaLokace())
        self.add_widget(self.snake[0])
        self.add_widget(self.jidlo)
        self.smer = 'doprava'
        Clock.schedule_interval(self.pohyb_kont, 1)


    def pohyb_kont(self, dt):
        dx = 0
        dy = 1100
        if self.smer == 'nahoru':
            self.snake[0].pohyb(0, 50)
        elif self.smer == 'dolu':
            self.snake[0].pohyb(0, -50)
        elif self.smer == 'doleva':
            self.snake[0].pohyb(-50, 0)
        elif self.smer == 'doprava':
            self.snake[0].pohyb(50, 0)

        novy_x = self.snake[0].pos[0] + dx
        novy_y = self.snake[0].pos[1] + dy

        #print(novy_x, novy_y) #0-650 sirka
        #print(f"Pozice jídla: {self.pos}")
        if novy_x > 650:
            self.snake[0].pohyb(-50, 0)
        elif novy_x < 0:
            self.snake[0].pohyb(50, 0)
        elif novy_y > 2250:
            self.snake[0].pohyb(0,-50)
        elif novy_y < 2100:
            self.snake[0].pohyb(0,50)
        
        if self.snake[0].collide_widget(self.jidlo):
            dx = abs(self.snake[0].center_x - self.jidlo.center_x)
            dy = abs(self.snake[0].center_y - self.jidlo.center_y)
            if dx < 50 / 2 and dy < 50 / 2:  # polovina velikosti widgetu
                print(True)
                self.jidlo.premisti()
                nova_cast_tela = SnakeTelo(self.snake[-1].pos)
                self.snake.append(nova_cast_tela)
                self.add_widget(nova_cast_tela)

        for i in range(len(self.snake)-1, 0, -1):
            self.snake[i].pos = self.snake[i-1].pos
            self.snake[i].rect.pos = self.snake[i].pos

    def pohyb_nahoru(self, instance):
        if self.smer != 'dolu':
            self.smer = 'nahoru'

    def pohyb_dolu(self, instance):
        if self.smer != 'nahoru':
            self.smer = 'dolu'

    def pohyb_vlevo(self, instance):
        if self.smer != 'doprava':
            self.smer = 'doleva'

    def pohyb_vpravo(self, instance):
        if self.smer != 'doleva':
            self.smer = 'doprava'

    def nahodnaLokace(self):
        #return [randint(0, 650), randint(1000,1170)]
        #return [randint(1, 13) * 50, randint(20,23) * 50]
        return [350, 1100]


class CalculatorManager(ScreenManager):
    pass

kv = Builder.load_file("./my.kv")

class MyApp(App):
    def build(self):
        if(platform == 'android' or platform == 'ios'):
            Window.maximize()
        else:
            Window.size = (350, 600)
        return kv


if __name__ == '__main__':
    MyApp().run() 
