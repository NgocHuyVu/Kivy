# Co je Kivy?
Kivy je open-source framework Pythonu, který umožňuje vytvořit apliakce pro Windows, Mac OS, Linux, Android, iOS, Raspberry-Pi.

# Co podporuje Kivy?
- multi-touch: je ideální pro tvorbu her a aplikací na dotyková zařížení
- multi-platform: vytvoříme kód jednou, pak může spouštět na různých operačních systémů a na různých zařízeních, tedy zobrazuje stejný a podobný pohled na všech platformách

# Instalance
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


class HelloWorld(App):
    def build(self):
        # Vrátí label, který se má zobrazit Hello World
        return Label(text ="Hello World")
    
if __name__ == "__main__":
    HelloWorld().run()
```

# Ovládací prvky = widget 
Kdy poutřebujeme použít prvek, tak nejprve musíme importovat pomocí vzoru: from kivy.uix.<nazev_prvek> import <Nazev_prvek>

- Label = slouží pro výpis
- Button = tlačítko pro zavolání metody
- TextInput = textové pole pro zadání textu od uživatele
- Checkbox
- Dropdown list
- ...
# Animace 

