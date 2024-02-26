# Co je Kivy?
Kivy je open-source framework Pythonu, který umožňuje vytvořit aplikace pro Windows, Mac OS, Linux, Android, iOS, Raspberry-Pi.

# Co podporuje Kivy?
- **multi-touch**: je ideální pro tvorbu her a aplikací na dotyková zařížení
- **multi-platform**: vytvoříme kód jednou, pak ho můžeme spouštět na různých operačních systémech a zařízeních, tedy zobrazuje stejný nebo podobný vzhled na všech platformách

# Instalace
```
py -m pip install kivy
```

# První aplikace 

**Úkol 1: Vytvořte aplikace Helloworld, která zobrazuje nějaký text na obrazovku pomocí prvku Label.**

Potřebujeme prvek (widget) **Label**, který slouží pro zápis textu. Bude zobrazovat HelloWord na obrázovku. 

Když poutřebujeme použít některý prvek, tak ho nejprve musíme importovat pomocí vzoru: 
**from kivy.uix.<nazev_prvek> import <Nazev_prvek>** 

V náš případě potřebujeme importovat Label.
from kivy.uix.label import Label

```
#importujme Kivy a další ovládací prvky např. label, button
import kivy
from kivy.app import App
from kivy.uix.label import Label

class HelloWorld(App):
    def build(self):
        # Vrátí label, který se má zobrazit Hello World
        return Label(text ="Hello World")
    
if __name__ == "__main__":
    HelloWorld().run()
```

**Úkol 2: Předchozí aplikace má bílý text. Změňte barvu text, aby je fialový ve formátu RGBA (0.41, 0.42, 0.74, 1)**
 - Mění barvu Label
   Nástroj umožňuje vybírat barvy a získávat k nim příslušné hodnoty RGB: https://rgbcolorpicker.com/0-1	
  ```
  class HelloWorld(App):
    def build(self):
        # Vrátí label, který se má zobrazit Hello World
        return Label(text ="Hello World", color =(0.41, 0.42, 0.74, 1))
  ```
  -  Pouzíváme **Text Markup**, aby můžeme měnit **formát textu**
    **[formát]text[/formát], markup = True**

 
  - [b][/b] -> tučný
  - [i][/i] -> kurzíva
  - [u][/u] -> podtržení
  - [s][/s] -> přeškrtnut
  - [font=][/font] ->  typ písma
  - [size=][/size]] ->  velikost písma
  - [color=#][/color] -> barva textu
  - [sub][/sub] -> zobrazí text na pozici dolního indexu vzhledem k textu před ním.
  - [sup][/sup] -> zobrazí text na pozici horního indexu vzhledem k textu před ním.

**Úkol 3: Zobrazuje text "Hello World" v tučném písmu.**
 ```
 class HelloWorld(App):
 def build(self):
 	# Vrátí label, který se má zobrazit Hello World
	return Label(text ="[b]Hello World[b]", color =(0.41, 0.42, 0.74, 1), markup = True)
  ```
    
# Kivy language

**Kivy language** se používá pro pozicování a vzhled aplikace. Má stejný účel jako css soubor. Kivy language kód píšeme do souboru s příponou .kv , díky tomu ho oddělíme od zdrojového logického kódu v Pythonu. Můžeme měnit vzhled aplikace pomocí Pythonu, ale jestliže používáme kivy language, pak kód je čitelnější, a je snadnější údržbu a správu aplikace.

Kivi soubor by se měl jmenovat stejně jako název třídy aplikace. Nemusí se nutně jmenovat stejně, ale pokud ho Kivy nenajde podle názvu třídy aplikace, museli bychom jej importovat ručně pomocí Builder.load_file(soubor)).

**Úkol 4: Pomocí Kivy language rozdělte část v Pythonu, která umožňuje pro vzhled aplikace, aby je psán do souboru .kv**

- helloworld.py
```
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class Grid(Widget):
    pass


class MyApp(App):
    def build(self):
        return Grid()


if __name__ == "__main__":
    MyApp().run()
```
- styl.kv
  
 ```
  <Grid>:
    GridLayout:
        cols:1
        size: root.width, root.height

        GridLayout:
            cols:1
            Label:
                text: "Hello World "
                color: 0.41, 0.42, 0.74, 1
                markup: True
 ```

  
# Layout 

**Layout** zajišťuje uspořádání a pozicování prvků GUI. Máme růžné typy rozložení:

**Úkol 4: Vytvořte vzhled jednoduché kalkulačky, která obsahuje čísla, operace +, -, *, /, a smázání**

Kalkulačka 

- app.py
  
```
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

Builder.load_file("./my.kv")

#velikost okna, sirka/vyska
Window.size = (350, 600) 

class Calculator(GridLayout):
    pass
    
class MyApp(App):
    def build(self):
        return Calculator()


if __name__ == '__main__':
    MyApp().run()
```

- **BoxLayout** = prvky jsou umístěny podle vertikální nebo horizontální směru.
  - my.kv
    ```
    <CalculatorWidget>:
        BoxLayout
            orientation: "vertical"
            size: root.width, root.height
    ```
-  **GridLayout** umožňuje umístit prvky ve maticovém tvaru, určíme počet řádků a sloupců. Prvky jsou umístěny od levého horního rohu, plní se aktuální řádku, a pak se přechází na další řádek.

- **FloatLayout** umožňuje umístit relativně prvky podle šířky a výšky okna. Růžné zařízení mají růžné rozměry, podle kterých budou prvky automaticky se přizpůsobit, mění jejich rozměry a pozice. Jestliže měníme velikost okna, taky prvky budou se přizpůsobit.
  
- **AnchorLayout** = prvky jsou umíštěny ve rohu nebo střed
  - **anchor_x**: "left", "right" a "center"
  - **anchor_y**: "top",  "bottom" a "center"
  - Např. Vlevo nahoře: anchor_x="left", anchor_y="top"
    
    ![image](https://github.com/NgocHuyVu/Kivy/assets/128366057/2301dfce-9c65-43c9-8dc0-46df86447e4b)

- **RelativeLayout** umožňuje umístit relativně prvky podle šířky a výšky Layout
  
  
# Ovládací prvky = widget 
Kdy poutřebujeme použít některý prvek, tak nejprve musíme importovat pomocí vzoru: 
**from kivy.uix.<nazev_prvek> import <Nazev_prvek>**  

- **TextInput** = textové pole pro zadání textu od uživatele
  V naší kalkulačceje potřeba použít TextInput, které zobrazují vstupu a výstupu.
   ```
   <CalculatorWidget>:
    BoxLayout
        orientation: "vertical"
        size: root.width, root.height

        TextInput:
            id: vstup
            text: "0"
            font_size: 64
            multiline: False
            disabled: True # zakaze psat do displeje
            halign: "right" #odkud kam se zapisuje
        
        TextInput:
            id: vystup
            text: ""
            font_size: 64
            multiline: False
            halign: "right" #odkud kam se zapisuje
    ```
  - multiline = víceřádkový pomocí Enter

- **Button** = tlačítko spouštějí se po stisknutí
    Dále potřebujeme vytvořit tlačítka kalkulačky, které jsou čísla a operace. Můžeme provést několik změn nebo přidání funkcí k tlačítkům.
  
  - **Styl**
    - font_size = velikost písma
    - background_color = barva pozadí
    - color = barvatextu
    - size = velikost
    - size_hint = relativní velikost tlačítka
      - size_hint=(None, None) = pevná velikost
    - pos = pozice tlačítka
    - border = kulaté rohy
      
      např. border = (30, 30, 30, 30)
      
      
  - **Přídání fotky do pozadí tlačítka**
    - background_normal =  zobrazí, kdy není stisknuto
    - background_down = zobrazí, kdy je stisknuto
    - background_disabled_normal = zobrazí, kdy není stisknuto a zároveň není aktivováno
      
  - **Funkce**

    Používáme **on_press** pro přídání funkce. Pokud uživatel stiskne tlačítko, tak volá funkce
    
    ```
    <CalculatorWidget>:
        BoxLayout:
            id: rezim
            orientation: "vertical"
            size: root.width, root.height
    
            TextInput:
                id: vstup
                text: "0"
                font_size: 32
                multiline: True
                disabled: True 
                halign: "right"
                size_hint_y: None
                height: 64
            
            TextInput:
                id: vystup
                text: ""
                font_size: 32
                multiline: True
                disabled: True 
                halign: "right" #odkud kam se zapisuje
                size_hint_y: None
                height: 128
    
            GridLayout: #udava pocet sloupcu, radku
                cols: 4
                rows: 5
                
                # Sloupec 1
    
                Button:
                    id: rezim_button_19
                    text: "AC"
                    font_size: 32
                    on_press: root.smaz()
                    background_color: (0, 0, 0, 1)if root.ids.vstup.text == 'Error' else (0.7, 0.7, 0.7, 1)
                
                Button:
                    id: rezim_button_22
                    text: "C"
                    font_size: 32
                    on_press: root.vymaz_jedno()
                    background_color: (0.7, 0.7, 0.7, 1)
                
                Button:
                    font_size: 32
                    on_press: root.zmen_rezim()
                    background_normal: 'Day_night.jpeg'
    
                Button:
                    background_normal: 'veda.jpg'
                    font_size: 32
                    #on_press: root.vedecka_kalkulacka_velikost()  
                    #on_press: root.current = 'sc_kalkulacka'
                    on_release: app.root.current = "second"
    
                # SLOUPEC 2
                Button:
                    id: rezim_button_5
                    text: "7"
                    font_size: 32
                    on_press: root.cisla(7) if root.ids.vstup.text[-1] not in ('=') else None
                    background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)
    
                Button:
                    id: rezim_button_6
                    text: "8"
                    font_size: 32
                    on_press: root.cisla(8) if root.ids.vstup.text[-1] not in ('=') else None
                    background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)
    
                Button:
                    id: rezim_button_7
                    text: "9"
                    font_size: 32
                    on_press: root.cisla(9) if root.ids.vstup.text[-1] not in ('=') else None
                    background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)
    
                Button:
                    id: rezim_button_8
                    text: "*"
                    font_size: 32
                    on_press: root.operace("*") 
                    background_color: (0.7, 0.7, 0.7, 1)
    
                # SLOUPEC 3
                Button:
                    id: rezim_button_9
                    text: "4"
                    font_size: 32
                    on_press: root.cisla(4) if root.ids.vstup.text[-1] not in ('=') else None
                    background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)
    
                Button:
                    id: rezim_button_10
                    text: "5"
                    font_size: 32
                    on_press: root.cisla(5) if root.ids.vstup.text[-1] not in ('=') else None
                    background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)
    
                Button:
                    id: rezim_button_11
                    text: "6"
                    font_size: 32
                    on_press: root.cisla(6) if root.ids.vstup.text[-1] not in ('=') else None
                    background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)
    
                Button:
                    id: rezim_button_12
                    text: "-"
                    font_size: 32
                    on_press: root.operace("-")
                    background_color: (0.7, 0.7, 0.7, 1)
    
                # SLOUPEC 4
                Button:
                    id: rezim_button_13
                    text: "1"
                    font_size: 32
                    on_press: root.cisla(1) if root.ids.vstup.text[-1] not in ('=') else None
                    background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)
    
                Button:
                    id: rezim_button_14
                    text: "2"
                    font_size: 32
                    on_press: root.cisla(2) if root.ids.vstup.text[-1] not in ('=') else None
                    background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)
    
                Button:
                    id: rezim_button_15
                    text: "3"
                    font_size: 32
                    on_press: root.cisla(3) if root.ids.vstup.text[-1] not in ('=') else None
                    background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)
    
    
                Button:
                    id: rezim_button_16
                    text: "+"
                    font_size: 32
                    on_press: root.operace("+") 
                    background_color: (0.7, 0.7, 0.7, 1)
    
                # SLOUPEC 5
                
                Button:
                    id: rezim_button_21
                    text: "."
                    font_size: 32
                    on_press: root.operace(".")
                    background_color: (0.7, 0.7, 0.7, 1)
    
                Button:
                    id: rezim_button_18
                    text: "0"
                    font_size: 32
                    on_press: root.cisla(0)
                    background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)
                 
                Button:
                    id: rezim_button_17
                    text: "="
                    font_size: 32
                    on_press: root.vypocitej()
                    background_color: (0.7, 0.7, 0.7, 1)

                Button:
                    id: rezim_button_20
                    text: "/"
                    font_size: 32
                    on_press: root.operace("/")
                    background_color: (0.7, 0.7, 0.7, 1)
    ```

    - app.py
    ```
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
            else:
                self.ids.vstup.text  = (f"{vstup_cisla}{cislo}") #pridava cisla
        
        def pridej_znak(self, znak):
            znaky = ["+", "-", "*", "/"]
            vstup_znaku = self.ids.vstup.text
    
            if vstup_znaku[-1] in znaky or (len(vstup_znaku) < 2 and vstup_znaku == 0): # logiku aby neslo pridat znamenko 1.
                pass
            else:
                self.ids.vstup.text  = (f"{vstup_znaku}{znak}")
        
        def vypocitej(self): #nakonec jsem udelal to pocitani, jen tam osetri deleni 0 a asi nejspis pridej horizontalni polohu
            vstup = self.ids.vstup.text
            self.ids.vystup.text = str(eval(vstup))
        
    class MyApp(App):
        def build(self):
            return CalculatorWidget()
    
    
    if __name__ == '__main__':
        MyApp().run() #my.kv se spousti podle tridy MyApp, neco jako C# oddeli velky pismena jako slovo
    ```
Kivy má další různé prvky (widget), např. 

- **Label** = slouží pro výpis

  - Mění barvu Label

  ```
  class HelloWorld(App):
    def build(self):
        # Vrátí label, který se má zobrazit Hello World
        return Label(text ="Hello World", color =(0.41, 0.42, 0.74, 1))
  ```
    Pouzíváme Text Markup, aby můžeme měnit styl textu
    [styl]text[/styl]

  ```
  class HelloWorld(App):
  def build(self):
      # Vrátí label, který se má zobrazit Hello World
      return Label(text ="[b]Hello World[b]", color =(0.41, 0.42, 0.74, 1), markup = True)
  ```
  - [b][/b] -> tučný
  - [i][/i] -> kurzíva
  - [u][/u] -> Podtržení
  - [s][/s] -> Přeškrtnut
  - [font=][/font] ->  typ písma
  - [size=][/size]] ->  velikost písma
  - [color=#][/color] -> barva textu
  - [sub][/sub] -> Zobrazí text na pozici dolního indexu vzhledem k textu před ním.
  - [sup][/sup] -> Zobrazí text na pozici horního indexu vzhledem k textu před ním.
  
    


- **Checkbox** umožňuje provést dvě volbu, např. ano nebo ne
```
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout


# Container class for the app's widgets
class check_box(GridLayout):

	def __init__(self, **kwargs):
		super(check_box, self).__init__(**kwargs)

		# 2 columns in grid layout
		self.cols = 2

		# Add checkbox, widget and labels
		self.add_widget(Label(text ='Muž'))
		self.active = CheckBox(active = True)
		self.add_widget(self.active)

		self.add_widget(Label(text ='Žena'))
		self.active = CheckBox(active = True)
		self.add_widget(self.active)

		self.add_widget(Label(text ='Jiný'))
		self.active = CheckBox(active = True)
		self.add_widget(self.active)

	
class CheckBoxApp(App):
	def build(self):	 
		return check_box()

if __name__ == '__main__':
	CheckBoxApp().run()

```

- **Dropdown list** umožňuje zobrazit seznam voleb. Může být tlačítko, fotka, ...
  
```
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
```

- **Scrollview** umožňuje uživatelům posouvat obsah (například text, obrázky nebo další widgety) v rámci určené oblasti, která je ohraničena velikostí ScrollView
```
```

# Navigace mezi multi-screen

**Úkol 5: Vytvořte vědeckou kalkulačku, která obsahuje druhou mocninu, třetí mocninu, odmocninu, ...**

Import modulů
```
from kivy.uix.screenmanager import ScreenManager, Screen
```

Pro každé kalkulačky, které bychom chtěli vytvořit, musíme vytvořit třídy CalculatorWidget a ScienceCalculatorWidget, které dědí z třídy Screen. Pokud budeme pracovat s více než jedním oknem, musíme vytvořit třídu CalculatorManager, která bude řídit navigaci mezi těmito okny. Tato třída bude muset zdědit ze ScreenManager.
```
class CalculatorWidget(Screen):
    temp_cislo = "" #pro to abychom mohli tamto cos chtel
    #rezim_barva = 0
    rezim_velikost = 0

    def smaz(self): #funkce na mazani, je tam chyba
        self.ids.vstup.text = "0"
        self.ids.vystup.text = ""
        CalculatorWidget.temp_cislo = ""

    def vymaz_jedno(self):
        self.ids.vstup.text = self.ids.vstup.text[:-1]

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
    
    def zmen_rezim(self):
        for button_id in self.ids.keys():
            button = self.ids[button_id]
            if isinstance(button, Button):
                if button.background_color == [0, 1, 1, 1]:
                    button.background_color = [0.7, 0.7, 0.7, 1]
                else:
                    button.background_color = [0, 1, 1, 1]
    
    def vedecka_kalkulacka_velikost(self):
        if CalculatorWidget.rezim_velikost == 0:
            Window.size = (600,350)
            CalculatorWidget.rezim_velikost = 1
            #self.sm.current = "sc_kalkulacka"
            #Builder.unload_file("./my.kv")
        else:
            Window.size = (350,600)
            CalculatorWidget.rezim_velikost = 0

class ScienceCalculatorWidget(Screen):
    temp_cislo = "" #pro to abychom mohli tamto cos chtel
    #rezim_barva = 0
    rezim_velikost = 0

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
    
    def zmen_rezim(self):
        for button_id in self.ids.keys():
            button = self.ids[button_id]
            if isinstance(button, Button):
                if button.background_color == [0, 1, 1, 1]:
                    button.background_color = [0.7, 0.7, 0.7, 1]
                else:
                    button.background_color = [0, 1, 1, 1]
    
    def vedecka_kalkulacka_velikost(self):
        if CalculatorWidget.rezim_velikost == 0:
            Window.size = (600,350)
            CalculatorWidget.rezim_velikost = 1
            #self.sm.current = "sc_kalkulacka"
            #Builder.unload_file("./my.kv")
        else:
            Window.size = (350,600)
            CalculatorWidget.rezim_velikost = 0


class CalculatorManager(ScreenManager):
    pass
```

GUI
```
CalculatorManager:
    CalculatorWidget:
    ScienceCalculatorWidget:

<CalculatorWidget>:
    name: "prvni"

    BoxLayout:
        id: rezim
        orientation: "vertical"

        TextInput:
            id: vstup
            text: "0"
            font_size: 32
            multiline: True
            readonly: True
            halign: "right" #odkud kam se zapisuje
            size_hint_y: None
            height: 64
        
        TextInput:
            id: vystup
            text: ""
            font_size: 32
            multiline: True
            readonly: True
            halign: "right" #odkud kam se zapisuje
            size_hint_y: None
            height: 128

        GridLayout: #udava pocet sloupcu, radku
            cols: 4
            rows: 6
            
            # Sloupec 1

            Button:
                id: rezim_button_1
                text: "AC"
                font_size: 32
                on_press: root.smaz()
                background_color: (0, 0, 0, 1)if root.ids.vstup.text == 'Error' else (0.7, 0.7, 0.7, 1)
            
            Button:
                id: rezim_button_2
                text: "C"
                font_size: 32
                on_press: root.vymaz_jedno()
                background_color: (0.7, 0.7, 0.7, 1)
            
            Button:
                font_size: 32
                on_press: root.zmen_rezim()
                background_normal: 'Day_night.jpeg'

            Button:
                background_normal: 'veda.jpg'
                font_size: 32
                #on_press: root.vedecka_kalkulacka_velikost()  
                #on_press: root.current = 'sc_kalkulacka'
                on_release: 
                    root.vedecka_kalkulacka_velikost()  
                    app.root.current = "druhy"
                    root.manager.transition.direction = "left"

            # SLOUPEC 2
            Button:
                id: rezim_button_3
                text: "7"
                font_size: 32
                on_press: root.cisla(7) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_4
                text: "8"
                font_size: 32
                on_press: root.cisla(8) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_5
                text: "9"
                font_size: 32
                on_press: root.cisla(9) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_6
                text: "*"
                font_size: 32
                on_press: root.operace("*") 
                background_color: (0.7, 0.7, 0.7, 1)

            # SLOUPEC 3
            Button:
                id: rezim_button_7
                text: "4"
                font_size: 32
                on_press: root.cisla(4) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_8
                text: "5"
                font_size: 32
                on_press: root.cisla(5) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_9
                text: "6"
                font_size: 32
                on_press: root.cisla(6) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_10
                text: "-"
                font_size: 32
                on_press: root.operace("-")
                background_color: (0.7, 0.7, 0.7, 1)

            # SLOUPEC 4
            Button:
                id: rezim_button_11
                text: "1"
                font_size: 32
                on_press: root.cisla(1) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_12
                text: "2"
                font_size: 32
                on_press: root.cisla(2) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_13
                text: "3"
                font_size: 32
                on_press: root.cisla(3) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)


            Button:
                id: rezim_button_14
                text: "+"
                font_size: 32
                on_press: root.operace("+") 
                background_color: (0.7, 0.7, 0.7, 1)

            # SLOUPEC 5
            
            Button:
                id: rezim_button_15
                text: "."
                font_size: 32
                on_press: root.operace(".")
                background_color: (0.7, 0.7, 0.7, 1)
            Button:
                id: rezim_button_16
                text: "0"
                font_size: 32
                on_press: root.cisla(0)
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)
            

            Button:
                id: rezim_button_17
                text: "="
                font_size: 32
                on_press: root.vypocitej()
                background_color: (0.7, 0.7, 0.7, 1)
            

            Button:
                id: rezim_button_18
                text: "/"
                font_size: 32
                on_press: root.operace("/")
                background_color: (0.7, 0.7, 0.7, 1)
            
        Button:
            id: rezim_button_19
            text: "had"
            font_size: 32
            size_hint_y : None
            background_color: (0.7, 0.7, 0.7, 1)
            on_release: 
                app.root.current = "snake"
                #root.manager.transition: NoTransition
                root.manager.transition.direction = "down"


###################################################################
###################################################################
###################################################################
<ScienceCalculatorWidget>:
    name: "druhy"

    BoxLayout:
        id: rezim
        orientation: "vertical"
        #orientation: "horizontal" pozdeji jeste prepsat 
        size: root.width, root.height

        TextInput:
            id: vstup
            text: "0"
            font_size: 32
            multiline: True
            readonly: True
            halign: "right" #odkud kam se zapisuje
            size_hint_y: None
            height: 64
        
        TextInput:
            id: vystup
            text: ""
            font_size: 32
            multiline: True
            readonly: True
            halign: "right" #odkud kam se zapisuje
            size_hint_y: None
            height: 128

        GridLayout: #udava pocet sloupcu, radku
            cols: 4
            rows: 7

            # Sloupec 1

            Button:
                id: rezim_button_1
                text: "AC"
                font_size: 32
                on_press: root.smaz()
                background_color: (0, 0, 0, 1)if root.ids.vstup.text == 'Error' else (0.7, 0.7, 0.7, 1)
            
            Button:
                id: rezim_button_2
                text: "C"
                font_size: 32
                on_press: root.vymaz_jedno()
                background_color: (0.7, 0.7, 0.7, 1)
            
            Button:
                font_size: 32
                on_press: root.zmen_rezim()
                background_normal: 'Day_night.jpeg'

            Button:
                background_normal: 'veda.jpg'
                font_size: 32
                #on_press: root.vedecka_kalkulacka_velikost()  
                #on_press: root.current = 'sc_kalkulacka'
                on_release:
                    root.vedecka_kalkulacka_velikost()  
                    app.root.current = "prvni"
                    root.manager.transition.direction = "right"

            # SLOUPEC 2

            #Pokud už používá operace +,-,/,*,= tak nejde použivat vedeckou operace
            Button:
                id: rezim_button_3
                text: "1/x"
                font_size: 32
                on_press: root.vedecka_kalkulacka("1/x") if not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else (0, 0, 0, 1)

            Button:
                id: rezim_button_4
                text: "x^2"
                font_size: 32
                on_press: root.vedecka_kalkulacka("x^2") if not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else (0, 0, 0, 1)

            Button:
                id: rezim_button_5
                text: "x^3"
                font_size: 32
                on_press: root.vedecka_kalkulacka("x^3") if not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else (0, 0, 0, 1)

            Button:
                id: rezim_button_6
                text: "√"
                font_size: 32
                on_press: root.vedecka_kalkulacka("√") if not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else (0, 0, 0, 1)


            # SLOUPEC 3
            Button:
                id: rezim_button_7
                text: "10^x"
                font_size: 32
                on_press: root.vedecka_kalkulacka("10^x") if not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else (0, 0, 0, 1)

            Button:
                id: rezim_button_8
                text: "π" #PI
                font_size: 32
                on_press: root.cisla("PI") if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_9
                text: "log"
                font_size: 32
                on_press: root.vedecka_kalkulacka("log") if not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else (0, 0, 0, 1)

            Button:
                id: rezim_button_10
                text: "ln"
                font_size: 32
                on_press: root.vedecka_kalkulacka("ln") if not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else (0, 0, 0, 1)

            # SLOUPEC 3
            Button:
                id: rezim_button_11
                text: "7"
                font_size: 32
                on_press: root.cisla(7) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_12
                text: "8"
                font_size: 32
                on_press: root.cisla(8) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_13
                text: "9"
                font_size: 32
                on_press: root.cisla(9) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_14
                text: "*"
                font_size: 32
                on_press: root.operace("*") 
                background_color: (0.7, 0.7, 0.7, 1)

            # SLOUPEC 4
            Button:
                id: rezim_button_15
                text: "4"
                font_size: 32
                on_press: root.cisla(4) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_16
                text: "5"
                font_size: 32
                on_press: root.cisla(5) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_17
                text: "6"
                font_size: 32
                on_press: root.cisla(6) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_18
                text: "-"
                font_size: 32
                on_press: root.operace("-")
                background_color: (0.7, 0.7, 0.7, 1)

            # SLOUPEC 5
            Button:
                id: rezim_button_19
                text: "1"
                font_size: 32
                on_press: root.cisla(1) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_20
                text: "2"
                font_size: 32
                on_press: root.cisla(2) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_21
                text: "3"
                font_size: 32
                on_press: root.cisla(3) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)


            Button:
                id: rezim_button_22
                text: "+"
                font_size: 32
                on_press: root.operace("+") 
                background_color: (0.7, 0.7, 0.7, 1)

            # SLOUPEC 6
            
            Button:
                id: rezim_button_23
                text: "."
                font_size: 32
                on_press: root.operace(".")
                background_color: (0.7, 0.7, 0.7, 1)
            Button:
                id: rezim_button_24
                text: "0"
                font_size: 32
                on_press: root.cisla(0)
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)
            

            Button:
                id: rezim_button_25
                text: "="
                font_size: 32
                on_press: root.vypocitej()
                background_color: (0.7, 0.7, 0.7, 1)
            Button:
                id: rezim_button_26
                text: "/"
                font_size: 32
                on_press: root.operace("/")
                background_color: (0.7, 0.7, 0.7, 1)
```
