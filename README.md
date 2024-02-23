# Co je Kivy?
Kivy je open-source framework Pythonu, který umožňuje vytvořit aplikace pro Windows, Mac OS, Linux, Android, iOS, Raspberry-Pi.

# Co podporuje Kivy?
- multi-touch: je ideální pro tvorbu her a aplikací na dotyková zařížení
- multi-platform: vytvoříme kód jednou, pak ho můžeme spouštět na různých operačních systémech a zařízeních, tedy zobrazuje stejný a podobný vzhled na všech platformách

# Instalace
```
py -m pip install kivy
```

# Vzor kódu = Hello World
```
#importujme Kivy a další ovládací prvky např. label, button
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class HelloWorld(App):
    def build(self):
        # Vrátí label, který se má zobrazit Hello World
        return Label(text ="Hello World")
    
if __name__ == "__main__":
    # Spouští instance třídy, a vytvoří windows
    HelloWorld().run()
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
    [b][/b] -> tučný
    [i][/i] -> kurzíva
    [u][/u] -> Podtržení
    [s][/s] -> Přeškrtnut
    [font=][/font] ->  typ písma
    [size=][/size]] ->  velikost písma
    [color=#][/color] -> barva textu
    [sub][/sub] -> Zobrazí text na pozici dolního indexu vzhledem k textu před ním.
    [sup][/sup] -> Zobrazí text na pozici horního indexu vzhledem k textu před ním.
  
- TextInput = textové pole pro zadání textu od uživatele
  
- Button = tlačítko pro zavolání metody

- Checkbox
- Dropdown list
- ...
# Animace 

