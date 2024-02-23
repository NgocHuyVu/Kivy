# Co je Kivy?
Kivy je open-source framework Pythonu, který umožňuje vytvořit aplikace pro Windows, Mac OS, Linux, Android, iOS, Raspberry-Pi.

# Co podporuje Kivy?
- multi-touch: je ideální pro tvorbu her a aplikací na dotyková zařížení
- multi-platform: vytvoříme kód jednou, pak ho můžeme spouštět na různých operačních systémech a zařízeních, tedy zobrazuje stejný a podobný vzhled na všech platformách

# Instalace
```
py -m pip install kivy
```

# Layout 

Layout zajišťuje uspořádání a pozicování prvků GUI. Máme růžné typy rozložení:
- FloatLayout umožňuje umístit relativně prvky podle šírky a výšky okna. Růžné zařížení mají růžné rozměry, podle kterých budou prvky automaticky se přizpůsobit, mění jejich rozměry a pozice. Jetliže měníme velkikost okna, taky prvky budou se přizpůsobit.
  
- BoxLayout = prvky jsou umíštěny podle vertikální a horizontální směru.
  
- AnchorLayout = prvky jsou umíštěny ve rohu nebo střed
  - anchor_x: "left", "right" a "center"
  - anchor_y: "top",  "bottom" a "center"
  - Např. anchor_x="left", anchor_y="top"
    
    ![image](https://github.com/NgocHuyVu/Kivy/assets/128366057/2301dfce-9c65-43c9-8dc0-46df86447e4b)

- RelativeLayout umožňuje umístit relativně prvky podle šírky a výšky Layout
  
- GridLayout umožňuje umíštit prvky ve maticovém tvaru, určíme počet řádků a sloupců. Prvky jsou umíštěny od levého horního rohu, plní se aktuální řádku, a pak se přechází na další řádek.
  
```
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


class MyApp(App):
    def build(self):
        return Calculator()

if __name__ == '__main__':
    MyApp().run()
```


# Ovládací prvky = widget 
Kdy poutřebujeme použít některý prvek, tak nejprve musíme importovat pomocí vzoru: 
from kivy.uix.<nazev_prvek> import <Nazev_prvek>  


- Label = slouží pro výpis
  Mění barvu Label

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
  
- TextInput = textové pole pro zadání textu od uživatele
  ```
  TextInput(text='Hello world', multiline=False)
  ```
  - multiline = víceřádkový pomocí Enter
    
- Button = tlačítko pro zavolání metody

- Checkbox
- Dropdown list
- ...
# Animace 

