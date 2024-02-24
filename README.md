# Co je Kivy?
Kivy je open-source framework Pythonu, který umožňuje vytvořit aplikace pro Windows, Mac OS, Linux, Android, iOS, Raspberry-Pi.

# Co podporuje Kivy?
- **multi-touch**: je ideální pro tvorbu her a aplikací na dotyková zařížení
- **multi-platform**: vytvoříme kód jednou, pak ho můžeme spouštět na různých operačních systémech a zařízeních, tedy zobrazuje stejný a podobný vzhled na všech platformách

# Instalace
```
py -m pip install kivy
```

# První aplikace 

Kdy poutřebujeme použít některý prvek, tak nejprve musíme importovat pomocí vzoru: 
**from kivy.uix.<nazev_prvek> import <Nazev_prvek>** 

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

Label je prvek (widget), který slouží pro zápis textu. Můžeme měnit jeho vzhled

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

 - Mění barvu Label

  ```
  class HelloWorld(App):
    def build(self):
        # Vrátí label, který se má zobrazit Hello World
        return Label(text ="Hello World", color =(0.41, 0.42, 0.74, 1))
  ```
  -  Pouzíváme Text Markup, aby můžeme měnit styl textu
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
    
# Kivy language

Kivy language se používá pro pozicování a vzhled aplikace. Má stejný účel jako css soubor. Kivy language kód píšeme do souboru s příponou .kv , díky tomu oděllíme od zdrojového kódu v Pythonu. Můžeme měnit vzhled aplikace pomocí Pythonu, ale jestliže používáme kivy jazyk, pak kód je čitelnější. 

Kivi soubor by se měl jmenovat stejně jako název třídy aplikace. Nemusí se nutně jmenovat stejně, ale pokud ho Kivy nenajde podle názvu třídy aplikace, museli bychom jej importovat ručně pomocí Builder.load_file(soubor)).


- helloworld.py
```
#importujme Kivy a další ovládací prvky např. label, button
import kivy
from kivy.app import App
from kivy.uix.label import Label

class HelloWorld(App):
    def build(self):
        return Label(text="Hello World")

if __name__ == "__main__":
    HelloWorld().run()
```
- styl.kv
  
 ```
  <HelloWorld>:
    # Vzhled pro HelloWorld třídu
    Label:
        text: "[b]Hello World[/b]"
        color: 0.41, 0.42, 0.74, 1
        markup: True
 ```

  
# Layout 

**Layout** zajišťuje uspořádání a pozicování prvků GUI. Máme růžné typy rozložení:
- **FloatLayout** umožňuje umístit relativně prvky podle šírky a výšky okna. Růžné zařížení mají růžné rozměry, podle kterých budou prvky automaticky se přizpůsobit, mění jejich rozměry a pozice. Jetliže měníme velkikost okna, taky prvky budou se přizpůsobit.
  
  
- **AnchorLayout** = prvky jsou umíštěny ve rohu nebo střed
  - **anchor_x**: "left", "right" a "center"
  - **anchor_y**: "top",  "bottom" a "center"
  - Např. Vlevo nahoře: anchor_x="left", anchor_y="top"
    
    ![image](https://github.com/NgocHuyVu/Kivy/assets/128366057/2301dfce-9c65-43c9-8dc0-46df86447e4b)

- **RelativeLayout** umožňuje umístit relativně prvky podle šírky a výšky Layout
  
- **GridLayout** umožňuje umíštit prvky ve maticovém tvaru, určíme počet řádků a sloupců. Prvky jsou umíštěny od levého horního rohu, plní se aktuální řádku, a pak se přechází na další řádek.
  
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


- **BoxLayout** = prvky jsou umíštěny podle vertikální a horizontální směru.
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
        # vytvoření displaye
        display = BoxLayout(orientation="vertical", size_hint_x = "3") 


class MyApp(App):
    def build(self):
        return Calculator()

if __name__ == '__main__':
    MyApp().run()
```
  
# Ovládací prvky = widget 
Kdy poutřebujeme použít některý prvek, tak nejprve musíme importovat pomocí vzoru: 
**from kivy.uix.<nazev_prvek> import <Nazev_prvek>**  

- **Button** = tlačítko spouštějí se po stisknutí
  - **Vytvoření tlačítka**
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
        # vytvoření displaye
        display = BoxLayout(orientation="vertical", size_hint_x = "3")
        self.add_widget(display)

        #Vytcoření tlačítek    
        self.add_widget(Button(text='1'))
        self.add_widget(Button(text='2'))
        self.add_widget(Button(text='3'))
        self.add_widget(Button(text='+'))
        self.add_widget(Button(text='4'))
        self.add_widget(Button(text='5'))
        self.add_widget(Button(text='6'))
        self.add_widget(Button(text='-'))
        self.add_widget(Button(text='7'))
        self.add_widget(Button(text='8'))
        self.add_widget(Button(text='9'))
        self.add_widget(Button(text='*'))
        self.add_widget(Button(text='/'))
        self.add_widget(Button(text='='))
        self.add_widget(Button(text='AC'))


class MyApp(App):
    def build(self):
        return Calculator()

if __name__ == '__main__':
    MyApp().run()
```
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
      
```
Tady bude změnit styl tlačítek
```
      
  - **Přídání fotky do pozadí tlačítka**
    - background_normal =  zobrazí, kdy není stisknuto
    - background_down = zobrazí, kdy je stisknuto
    - background_disabled_normal = zobrazí, kdy není stisknuto a zároveň není aktivováno
      
  - **Funkce**

    Používáme on_press pro přídání funkce. Pokud uživatel stiskne tlačítko, tak volá funkce 
    
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
        # vytvoření displaye
        display = BoxLayout(orientation="vertical", size_hint_x = "3")
        self.add_widget(display)

        #Vytvoření tlačítek
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
        self.add_widget(Button(text='AC', on_press=self.smaz))


class MyApp(App):
    def build(self):
        return Calculator()

if __name__ == '__main__':
    MyApp().run()
```
  
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
  
- **TextInput** = textové pole pro zadání textu od uživatele
  ```
  TextInput(text='Hello world', multiline=False)
  ```
  - multiline = víceřádkový pomocí Enter
    


- **Checkbox** = umožňuje provést dvě volbu, např. ano nebo ne

- **Dropdown list** = umožňuje zobrazit seznam voleb. Může být tlačítko, fotka, ...

- **Scrollview**
- **Carousel Widget**
- **Slider**
# Animace 

