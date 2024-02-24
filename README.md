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
  

**Layout** zajišťuje uspořádání a pozicování prvků GUI. Máme růžné typy rozložení:

- **BoxLayout** = prvky jsou umíštěny podle vertikální nebo horizontální směru.
  - my.kv
    ```
    <CalculatorWidget>:
        BoxLayout
            orientation: "vertical"
            size: root.width, root.height
    ```
-  **GridLayout** umožňuje umíštit prvky ve maticovém tvaru, určíme počet řádků a sloupců. Prvky jsou umíštěny od levého horního rohu, plní se aktuální řádku, a pak se přechází na další řádek.
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

        GridLayout: #udava pocet sloupcu, radku
            cols: 4
            rows: 5
  ```

- **FloatLayout** umožňuje umístit relativně prvky podle šírky a výšky okna. Růžné zařížení mají růžné rozměry, podle kterých budou prvky automaticky se přizpůsobit, mění jejich rozměry a pozice. Jetliže měníme velkikost okna, taky prvky budou se přizpůsobit.
  
- **AnchorLayout** = prvky jsou umíštěny ve rohu nebo střed
  - **anchor_x**: "left", "right" a "center"
  - **anchor_y**: "top",  "bottom" a "center"
  - Např. Vlevo nahoře: anchor_x="left", anchor_y="top"
    
    ![image](https://github.com/NgocHuyVu/Kivy/assets/128366057/2301dfce-9c65-43c9-8dc0-46df86447e4b)

- **RelativeLayout** umožňuje umístit relativně prvky podle šírky a výšky Layout
  
  
# Ovládací prvky = widget 
Kdy poutřebujeme použít některý prvek, tak nejprve musíme importovat pomocí vzoru: 
**from kivy.uix.<nazev_prvek> import <Nazev_prvek>**  

- **TextInput** = textové pole pro zadání textu od uživatele
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

        GridLayout: #udava pocet sloupcu, radku
            cols: 4
            rows: 5
    ```
  - multiline = víceřádkový pomocí Enter

- **Button** = tlačítko spouštějí se po stisknutí
  - **Vytvoření tlačítka**
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
    
            GridLayout: #udava pocet sloupcu, radku
                cols: 4
                rows: 5
    
                # SLOUPEC 1##################
                Button:
                    text: "1"
                    font_size: 32
    
                Button:
                    text: "2"
                    font_size: 32
    
                Button:
                    text: "3"
                    font_size: 32
    
                Button:
                    text: "+"
                    font_size: 32
    
                # SLOUPEC 2######################
                Button:
                    text: "4"
                    font_size: 32
    
                Button:
                    text: "5"
                    font_size: 32
    
                Button:
                    text: "6"
                    font_size: 32
    
                Button:
                    text: "-"
                    font_size: 32
    
                # SLOUPEC 3#######################
                Button:
                    text: "7"
                    font_size: 32
    
                Button:
                    text: "8"
                    font_size: 32
    
                Button:
                    text: "9"
                    font_size: 32
    
                Button:
                    text: "*"
                    font_size: 32
    
                # SLOUPEC 4########################
                Button:
                    text: "="
                    font_size: 32
    
                Button:
                    text: "0"
                    font_size: 32
                
                Button:
                    text: "AC"
                    font_size: 32
    
                Button:
                    text: "/"
                    font_size: 32

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
      
      
  - **Přídání fotky do pozadí tlačítka**
    - background_normal =  zobrazí, kdy není stisknuto
    - background_down = zobrazí, kdy je stisknuto
    - background_disabled_normal = zobrazí, kdy není stisknuto a zároveň není aktivováno
      
  - **Funkce**

    Používáme **on_press** pro přídání funkce. Pokud uživatel stiskne tlačítko, tak volá funkce
    
    
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

        GridLayout: #udava pocet sloupcu, radku
            cols: 4
            rows: 5

            # SLOUPEC 1##################
            Button:
                text: "1"
                font_size: 32
                on_press: root.tlacitka_cisla(1) #root je dulezitej, za tim jmeno funkce

            Button:
                text: "2"
                font_size: 32
                on_press: root.tlacitka_cisla(2)

            Button:
                text: "3"
                font_size: 32
                on_press: root.tlacitka_cisla(3)

            Button:
                text: "+"
                font_size: 32
                on_press: root.pridej_znak("+")

            # SLOUPEC 2######################
            Button:
                text: "4"
                font_size: 32
                on_press: root.tlacitka_cisla(4)

            Button:
                text: "5"
                font_size: 32
                on_press: root.tlacitka_cisla(5)

            Button:
                text: "6"
                font_size: 32
                on_press: root.tlacitka_cisla(6)

            Button:
                text: "-"
                font_size: 32
                on_press: root.pridej_znak("-")

            # SLOUPEC 3#######################
            Button:
                text: "7"
                font_size: 32
                on_press: root.tlacitka_cisla(7)

            Button:
                text: "8"
                font_size: 32
                on_press: root.tlacitka_cisla(8)

            Button:
                text: "9"
                font_size: 32
                on_press: root.tlacitka_cisla(9)

            Button:
                text: "*"
                font_size: 32
                on_press: root.pridej_znak("*")

            # SLOUPEC 4########################
            Button:
                text: "="
                font_size: 32
                on_press: root.vypocitej()

            Button:
                text: "0"
                font_size: 32
                on_press: root.tlacitka_cisla(0)
            
            Button:
                text: "AC"
                font_size: 32
                on_press: root.smaz()

            Button:
                text: "/"
                font_size: 32
                on_press: root.pridej_znak("/")
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
  
    


- **Checkbox** = umožňuje provést dvě volbu, např. ano nebo ne

- **Dropdown list** = umožňuje zobrazit seznam voleb. Může být tlačítko, fotka, ...

- **Scrollview**
- **Carousel Widget**
- **Slider**
# Animace 

