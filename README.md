# Co je Kivy?
Kivy je open-source framework Pythonu, který umožňuje vytvořit aplikace pro Windows, Mac OS, Linux, Android, iOS, Raspberry-Pi.

# Co podporuje Kivy?
- multi-touch: je ideální pro tvorbu her a aplikací na dotyková zařížení
- multi-platform: vytvoříme kód jednou, pak ho můžeme spouštět na různých operačních systémech a zařízeních, tedy zobrazuje stejný a podobný vzhled na všech platformách

# Instalace
```
py -m pip install kivy

Aktivace virtuálního prostředí

Windows
kivy_venv\Scripts\activate

Linux nebo macOS
source kivy_venv/bin/activate
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
        # Vrátí label, který zobrazí Hello World
        return Label(text ="Hello World")
    
if __name__ == "__main__":
    # Spouští instanci třídy, a vytvoří windows (máš na mysli okno?)
    HelloWorld().run()
```

# Ovládací prvky = widget 
Když potřebujeme použít některý prvek, tak musíme nejprve importovat pomocí vzoru: 
from kivy.uix.<nazev_prvku> import <nazev_prvku>

- Label = slouží pro výpis
  Mění barvu Labelu
  ```
  class HelloWorld(App):
    def build(self):
        # Vrátí label, který má zobrazit Hello World
        return Label(text ="Hello World", color =(0.41, 0.42, 0.74, 1))
  ```
    Používáme Text Markup, abychom mohli měnit styl textu
    [styl]text[/styl]
      ```
      class HelloWorld(App):
        def build(self):
            # Vrátí label, který má zobrazit Hello World
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

