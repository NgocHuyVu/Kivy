# Co je Kivy?
Kivy je open-source framework Pythonu, který umožňuje vytvořit aplikace pro Windows, Mac OS, Linux, Android, iOS, Raspberry-Pi.

# Co podporuje Kivy?
- **multi-touch**: je ideální pro tvorbu her a aplikací na dotyková zařížení
- **multi-platform**: vytvoříme kód jednou, pak ho můžeme spouštět na různých operačních systémech a zařízeních, tedy zobrazuje stejný nebo podobný vzhled na všech platformách
- **zvuk a video**

# Nevýhody
- Omezená podpora komunity
- Problémy s výkonem při složitých aplikacích

# Instalace
Vytvoření nového virtuální prostředí pro svůj projekt Kivy. Virtuální prostředí zabrání možným instalačním konfliktům s jinými verzemi a balíčky Pythonu. Je to volitelné, ale důrazně se doporučuje:
```
python -m venv kivy_venv
```
2. možnost
```
py -m pip install kivy
```
# Aktivace

Windows
```
kivy_venv\Scripts\activate
```
Linux nebo MacOS
```
source kivy_venv/bin/activate
```
# Widgets - Ovládací prvky
  
**BoxLayout**: Uspořádává své potomky do řady nebo sloupce, v závislosti na orientaci.
- Orientation: 'vertical' nebo 'horizontal'

**Button**: Tlačítko

**Label**: Zobrazení textu

**TextInput**: Používá se k získání vstupu od uživatele

**Image**: Zobrazení obrázku

**Slider**: Umožňuje uživatelům vybrat hodnotu posunem

**Switch**: Umožňuje uživatelům zapnout/vypnout stav

**CheckBox**: Umožňuje uživatelům vybrat nebo zrušit výběr

**Popup**: Překryvného okno

**ProgressBar**: Ukazuje průběh operace

**ScreenManager**: Spravuje více oken (Screen widgets). 
- Má metody jako add_widget (pro přidání okna),
- remove_widget (pro odebrání okna),
- current (pro získání nebo nastavení aktuálního okna) atd.

Pokud poutřebujeme použít některý prvek, tak ho nejprve musíme importovat pomocí vzoru: 

**from kivy.uix.<nazev_prvku> import <Nazev_prvku>**

# Atributy widgetů

**text, tlacitka...**
- color: barva písma
- background_color: barva pozadí
- Font_size: velikost písma
  
**TextInput**

- hint_text: nápověda
- password: vstup jako heslo
- multiline = víceřádkový pomocí Enter
- readonly: Pouze pro čtení, lze kopírovat
- halign: zarovnání

**Button**

- on_press, on_release, a on_state: Události, které se vyvolají při stisknutí, uvolnění a změně stavu tlačítka.
- background_normal a background_down: Obrázky použité pro výchozí grafické zobrazení, když je tlačítko stisknuto a nestisknuto.
- border = kulaté rohy
 -např. border = (30, 30, 30, 30)

**Text Markup**
- Pro použití markupu použijeme - markup: True

- [b][/b] -> tučný
- [i][/i] -> kurzíva
- [u][/u] -> podtržení
- [s][/s] -> přeškrtnut
- [font=][/font] ->  typ písma
- [size=][/size]] ->  velikost písma
- [color=#][/color] -> barva textu
- [sub][/sub] -> zobrazí text na pozici dolního indexu vzhledem k textu před ním.
- [sup][/sup] -> zobrazí text na pozici horního indexu vzhledem k textu před ním.

**Multimedia**
- source: zdroj
- allow_stretch: roztahování
- size: velikost

**Operace**

**Switch/CheckBox**
- active: 
  
**Slider/ProgressBar**
- max:
- min:
- value: současná hodnota
  
**Popup**
- Title: jméno okna
- Content: 
- size_hint:

# Layout 

**Layout** zajišťuje uspořádání a pozicování prvků GUI. Máme růžné typy rozložení:

-  **BoxLayout** uspořádává prvky buď ve vertikálním nebo horizontálním boxu.
  
-  **GridLayout** umožňuje umístit prvky v maticovém tvaru, určíme počet řádků a sloupců. Prvky jsou umístěny od levého horního rohu, plní se podle řádku, pak přechází na další řádek.

- **FloatLayout** umožňuje umístit relativně prvky podle šířky a výšky okna. Růžné zařízení mají růžné rozměry, podle kterých budou prvky automaticky přizpůsobovat, měnit jejich rozměry a pozice. Jestliže měníme velikost okna, tak se prvky budou přizpůsobovat.
  
- **AnchorLayout** = prvky jsou umíštěny v rohu nebo na středu
  - **anchor_x**: "left", "right" a "center"
  - **anchor_y**: "top",  "bottom" a "center"
  - Např. Vlevo nahoře: anchor_x="left", anchor_y="top"
    
    ![image](https://github.com/NgocHuyVu/Kivy/assets/128366057/2301dfce-9c65-43c9-8dc0-46df86447e4b)

- **RelativeLayout** umožňuje umístit relativně prvky podle šířky a výšky Layout

# Kivy language

Používá se pro pozicování a vzhled aplikace. 

Má podobný účel jako css soubor nebo html. 

Kivy language kód píšeme do souboru s příponou .kv , díky tomu ho **oddělíme od zdrojového logického kódu** v Pythonu.

Můžeme měnit vzhled aplikace přímo pomocí Pythonu, ale pokud používáme kivy language, pak je kód čitelnější, lepší pro údržbu a správu aplikace.

# Aplikace 

**Příklad 1: Aplikace, která zobrazuje nějaký text na obrazovce pomocí prvku Label.**

Potřebujeme prvek (widget) **Label**, který slouží pro zápis textu. Ten zobrazoví HelloWorld na obrázovce. 

Když poutřebujeme použít některý prvek, tak ho nejprve musíme importovat pomocí vzoru: 
**from kivy.uix.<nazev_prvek> import <Nazev_prvek>** 

**kivy.app**: Tento modul obsahuje App třídu, která je základem každé Kivy aplikace.

**kivy.uix**: Tento modul obsahuje třídy pro tvorbu uživatelského rozhraní (UI). uix v názvu modulu znamená “User Interface eXperience”.

**kivy.lang**: Tento modul obsahuje třídu Builder, která umožňuje vytvářet uživatelské rozhraní pomocí Kivy jazyka, což je jednoduchý jazyk speciálně navržený pro definování uživatelských rozhraní v Kivy.

V našem případě potřebujeme importovat Label.

```
from kivy.app import App
from kivy.uix.label import Label

class Priklad(App):
    def build(self):
        return Label(text='hi mom', color=(1,0,0))

Priklad().run()

```
**Příklad 1.1: Aplikace, která zobrazí text na obrazovce pomocí prvku Label za použítí kivy language.**
prvniAppka.py
```
from kivy.app import App
from kivy.lang.builder import Builder

kv = Builder.load_file("./prvniAppka.kv")

class Priklad(App):
    def build(self):
        return(kv)

Priklad().run()
```
prvniAppka.kv
```
Label:
    color: 1,0,0
    text: "Hi mom"
```
**Příklad 1.2: Aplikace, která zobrazí text na obrazovce pomocí prvku Label za použítí kivy language přímo v py.**
prvniAppka_loader.py
```
from kivy.app import App
from kivy.uix.label import Label
from kivy.lang.builder import Builder

class Priklad(App):
    def build(self):
        return Builder.load_string("""
Label:
    color: 1,0,0
    text: "Hi mom"                        
""")

Priklad().run()
```
**Příklad 2: Vytváření a přiřazení funkce**

funkce.py
```
from kivy.app import App
from kivy.lang.builder import Builder

kv = Builder.load_file("./funkce.kv")

class Priklad(App):
    def build(self):
        return kv
    
    def prepis(self):
        self.root.ids.vstup.text = 'Něco'

Priklad().run()
```
funkce.kv
```
BoxLayout:
    orientation: 'vertical'

    TextInput:
        id: vstup
        text: 'nic'
        font_size: 64
        #readonly: True
        #halign: "center" #left, center, right


    Button:
        text: 'ok'
        on_press: app.prepis()
```
**Příklad 2.1: Vytváření a přiřazení funkce v kivy language**

funkce_kv.py
```
from kivy.app import App
from kivy.lang.builder import Builder

kv = Builder.load_file("./funkce_kv.kv")

class Priklad(App):
    def build(self):
        return kv

Priklad().run()

```
funkce_kv.kv
```
BoxLayout:
    orientation: 'vertical'

    TextInput:
        id: vstup
        text: 'nic'
        font_size: 64
        #readonly: True
        #halign: "center" #left, center, right


    Button:
        text: 'ok'
        on_press: app.root.ids.vstup.text = "něco"
        #app referuje na instanci aplikace
        #root referu na kořen widgetu aplikace
        #ids je slovník všech widgetu v kv souboru
```
**Příklad 3: Vytvoření tlačítka, funkce, změna barvy**

- RGBA: red green blue alpha
- V kivy jsou barvy ve formátu 1 == 255
- [r/255.0, g/255.0, b/255.0, a/255.0]
- https://rgbcolorpicker.com/0-1

button_barvy.py
```
from kivy.app import App
from kivy.uix.button import Button
import random


class Priklad(App):
    def build(self):
        self.button = Button(text='Stiskni mě', background_color = (1,1,1,1))
        self.button.bind(on_press=self.klik) #bind přiřazení funkce
        return self.button

    def klik(self, instance):
        self.button.background_color = (random.random(),random.random(),random.random(),1)

Priklad().run()
```
**Příklad 3.1: Vytvoření tlačítka, funkce, změna barvy KV**

button_barvy_kv.py
```
from kivy.app import App
from kivy.lang.builder import Builder
import random

kv = Builder.load_file("./button_barvy.kv")

class Priklad(App):
    def build(self):
        return kv

    def klik(self):
        return (random.random(),random.random(),random.random(),1)

Priklad().run()
```

button_barvy_kv.kv
```
BoxLayout:
    orientation: 'vertical'
    Button:
        text: 'Stiskni mě'
        background_color: 1, 1, 1, 1
        on_press: self.background_color = app.klik()
```
**Příklad 4: Styly a jejich dědičnost**
```
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.clock import Clock
import random

kv = Builder.load_file("./styl.kv")

class Priklad(App):
    def zmen_barvu(self, dt): # dt = delta time, časový interval od posledního volání funkce
        self.root.ids.tlacitko_clock.background_color = [random.random() for _ in range(3)] + [1]

    def build(self):
        Clock.schedule_interval(self.zmen_barvu, 3)
        return kv

Priklad().run()

```
styl_kv.kv
```
<StylTlacitka@Button>:
    font_size: 20
    background_color: 1, 0, 0, 1 
    color: 1, 1, 1, 1

<NovyStylTlacitka@StylTlacitka>:
    font_size: 32

BoxLayout:
    StylTlacitka:
        text: 'Tlačítko 1'
    NovyStylTlacitka:
        id: tlacitko_clock
        text: 'Tlačítko 2'

```

**Příklad 5: Slider, ProgressBar a BoxLayout**

Slider.py
```
from kivy.app import App
from kivy.uix.slider import Slider
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar


class Priklad(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")
        slider = Slider(min=0, max=100, value=50)
        text = Label(text=str(slider.value))
        progress_bar = ProgressBar(max= slider.max, value = slider.value)

        def hodnota_slider(instance, value):
            text.text = str(value)
            progress_bar.value = int(value)

        slider.bind(value=hodnota_slider)
        layout.add_widget(text)
        layout.add_widget(slider)
        layout.add_widget(progress_bar)
        return layout

Priklad().run()
```
**Příklad 5.1: Slider, ProgressBar a BoxLayout**

Slider_kv.py
```
from kivy.app import App
from kivy.lang.builder import Builder

kv = Builder.load_file("./Slider.kv")


class Priklad(App):
    def build(self):
        return kv

Priklad().run()
```
Slider_kv.kv
```
BoxLayout:
    orientation: 'vertical'
    Label:
        id: my_label
        text: str(slider.value)
    Slider:
        id: slider
        min: 0
        max: 100
        value: 50
        on_value: my_label.text = str(self.value)
    ProgressBar:
        id: progress_bar
        max: 100
        value: slider.value
```
**Příklad 6: Multimedia**

multimedia.py
```
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import random

class Priklad(App):
    def otevri_popup(self, button):
        for i in range(10):
            popup = Popup(title='Testovací Popup', content=Button(text='Zavřít'), size_hint=(random.random(),random.random()))
            zavri_popup = Button(text='Zavřít')
            zavri_popup.bind(on_release=popup.dismiss)  # Přidáno
            popup.content = zavri_popup
            popup.pos_hint = {'x': random.random(), 'y': random.random()}
            popup.open()

    def build(self):
        button = Button(text='Otevři popup')
        button.bind(on_press=self.otevri_popup)
        return button

Priklad().run()
```


```
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader

class Priklad(App):
    def build(self):
        self.zvuk = SoundLoader.load('bird.mp3')
        if self.zvuk:
            print(f"Délka zvuku: {self.zvuk.length}")

        layout = BoxLayout(orientation='vertical')

        layout.add_widget(Image(source='pan.jpg'))

        button_layout = BoxLayout(orientation='horizontal')
        play_button = Button(text='Spusť')
        play_button.bind(on_press=self.play_sound)
        button_layout.add_widget(play_button)

        stop_button = Button(text='Zastav')
        stop_button.bind(on_press=self.stop_sound)
        button_layout.add_widget(stop_button)

        layout.add_widget(button_layout)

        return layout

    def play_sound(self, instance):
        self.zvuk.play()

    def stop_sound(self, instance):
        self.zvuk.stop()

Priklad().run()
```
**Příklad 6.1: Multimedia**
multimedia_kv.py
```
from kivy.app import App
from kivy.lang.builder import Builder

kv = Builder.load_file("./multimedia.kv")

class Priklad(App):
    def build(self):
        return kv

Priklad().run()
```
multimedia_kv.kv
```
BoxLayout:
    orientation: "vertical"

    GridLayout:
        row: 3
        cols: 3

        Image:
            source: "./pan.jpg"
            size_hint_y: None
            size: 100,100
            allow_stretch: True
        Image:
            source: "./pan.jpg"
        Image:
            source: "./pan.jpg"
        # sloupec 2
        Image:
            source: "./pan.jpg"
        Image:
            source: "./pan.jpg"
        Image:
            source: "./pan.jpg"
        Image:
            source: "./pan.jpg"
        Image:
            source: "./pan.jpg"
        Image:
            source: "./pan.jpg"
```
**Příklad 7: Popup**
```
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import random

class Priklad(App):
    def otevri_popup(self, button):
        for i in range(10):
            popup = Popup(title='Testovací Popup', content=Button(text='Zavřít'), size_hint=(random.random(),random.random()))
            zavri_popup = Button(text='Zavřít')
            zavri_popup.bind(on_release=popup.dismiss)  # Přidáno
            popup.content = zavri_popup
            popup.pos_hint = {'x': random.random(), 'y': random.random()}
            popup.open()

    def build(self):
        button = Button(text='Otevři popup')
        button.bind(on_press=self.otevri_popup)
        return button

Priklad().run()
```
**Příklad 8: Okna a jejich management**
multi_screen.py
```
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class ManagerScreen(ScreenManager):
    pass

kv = Builder.load_file("./multi_screen.kv")

class Priklad(App):
    def build(self):
        return kv

Priklad().run()

```
multi_screen.kv
```
ScreenManager:
    MenuScreen:
    SettingsScreen:

<MenuScreen>:
    name: "menu"

    BoxLayout:
        Button:
            text: 'do nastavení'
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = 'nastaveni'
        Label:
            text: "Menu"

<SettingsScreen>:
    name: "nastaveni"

    BoxLayout:
        Label:
            text: "Nastavení"
        Button:
            text: 'Zpět do menu'
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'menu'
```


# Cvičení - Kalkulačka
- Úkol 1: Vytvořte grafické uživatelské rozhraní kalkulačky. Kalkulačka obsahuje tláčika pro čísla, operace +, -, *, /, smázání, .... Dále obsahuje 2x TextInput. První TextInput slouží pro zadávání čísel a operací, která budou použita pro provedení vypočítání. Druhý TextInput slouží pro výpis výsledku
  
  ![image](https://github.com/NgocHuyVu/Kivy/assets/128366057/56aedebe-b500-45e8-bdd5-b872ea9568a4)

  Řešení
  
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
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import NoTransition
from kivy.metrics import dp
import math
from random import randint
from kivy.config import Config
from kivy.utils import platform


from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.clock import Clock


class CalculatorWidget(Screen):
    pass

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
```

my.kv
```
<Button@Button>
    #background_normal: ''
    font_size: "16sp"

<TextBox@TextInput>
    font_size: "16sp"
    readonly: True
    multiline: False
    halign: "right" #odkud kam se zapisuje


CalculatorManager:
    CalculatorWidget:

<CalculatorWidget>:
    name: "prvni"

    BoxLayout: #-- sestaveniElementu
        orientation: "vertical"

        TextBox:
            id: vstup
            text: "0"
            size_hint_y: None
            height: 64
        
        TextBox:
            id: vystup
            text: ""
            font_size: "32sp"
            size_hint_y: None
            height: 128

        GridLayout: #udava pocet sloupcu, radku
            cols: 4
            rows: 6
            
            # Sloupec 1

            Button:
                id: rezim_button_1
                text: "AC"
                background_color: (0, 0, 0, 1)
            
            Button:
                id: rezim_button_2
                text: "C"
                background_color: (0.7, 0.7, 0.7, 1)
            
            Button:
                #font_size: 32
                id: zmena_barvy
                background_normal: 'Day_night.jpeg'

            Button:
                background_normal: 'veda.jpg'
                id: prepnuti_kalkulacky
                #font_size: 32

            # SLOUPEC 2
            Button:
                id: rezim_button_3
                text: "7"
                background_color: (0.7, 0.7, 0.7, 1)

            Button:
                id: rezim_button_4
                text: "8"
                background_color: (0.7, 0.7, 0.7, 1)

            Button:
                id: rezim_button_5
                text: "9"
                background_color: (0.7, 0.7, 0.7, 1)

            Button:
                id: rezim_button_6
                text: "*"
                background_color: (0.7, 0.7, 0.7, 1)

            # SLOUPEC 3
            Button:
                id: rezim_button_7
                text: "4"
                background_color: (0.7, 0.7, 0.7, 1)

            Button:
                id: rezim_button_8
                text: "5"
                background_color: (0.7, 0.7, 0.7, 1)

            Button:
                id: rezim_button_9
                text: "6"
                background_color: (0.7, 0.7, 0.7, 1)

            Button:
                id: rezim_button_10
                text: "-"
                background_color: (0.7, 0.7, 0.7, 1)

            # SLOUPEC 4
            Button:
                id: rezim_button_11
                text: "1"
                background_color: (0.7, 0.7, 0.7, 1) 

            Button:
                id: rezim_button_12
                text: "2"
                background_color: (0.7, 0.7, 0.7, 1)

            Button:
                id: rezim_button_13
                text: "3"
                background_color: (0.7, 0.7, 0.7, 1)


            Button:
                id: rezim_button_14
                text: "+"
                #font_size: 32
                background_color: (0.7, 0.7, 0.7, 1)

            # SLOUPEC 5
            
            Button:
                id: rezim_button_15
                text: "."
                #font_size: 32
                background_color: (0.7, 0.7, 0.7, 1)
            Button:
                id: rezim_button_16
                text: "0"
                #font_size: 32
                background_color: (0.7, 0.7, 0.7, 1) 
            

            Button:
                id: rezim_button_17
                text: "="
                #font_size: 32
                background_color: (0.7, 0.7, 0.7, 1)
            

            Button:
                id: rezim_button_18
                text: "/"
                #font_size: 32
                background_color: (0.7, 0.7, 0.7, 1)
```

- Úkol 2: Implementace funkcí pro tlačítka s čísly

```
class CalculatorWidget(Screen):
    temp_cislo = ""
    def cisla(self, cislo): #funkce na cisla
        vstup_cisla = self.ids.vstup.text
        vystup_cisla = self.ids.vystup.text

        if vstup_cisla == "0":
            self.ids.vstup.text = ""
            self.ids.vstup.text += (f"{cislo}")
        elif vstup_cisla == "PI":
            self.ids.vstup.text += str(math.pi)
        else:
            self.ids.vstup.text  = (f"{vstup_cisla}{cislo}") #pridava cisla
```

- Úkol 3: Implementace funkcí pro operátory

```
class CalculatorWidget(Screen):
    temp_cislo = ""
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
```

- Úkol 4: Implementace funkce pro smázání

 
```
class CalculatorWidget(Screen):
    temp_cislo = ""
    def smaz(self):
        self.ids.vstup.text = "0"
        self.ids.vystup.text = ""
        CalculatorWidget.temp_cislo = ""

    def vymaz_jedno(self):
        if len(self.ids.vstup.text) > 1:
            self.ids.vstup.text = self.ids.vstup.text[:-1]
        else:
            self.ids.vstup.text = "0"

```
- Úkol 5: Vytvořte funkci, která slouží pro vrácení výsledku
```
class CalculatorWidget(Screen):
    temp_cislo = ""
    def vypocitej(self):
        vstup = self.ids.vstup.text
        try:
            self.ids.vystup.text = str(eval(vstup))
            self.ids.vstup.text  = self.ids.vstup.text + "="
            CalculatorWidget.temp_cislo = self.ids.vystup.text
        except:
            self.ids.vystup.text = "Error"
            self.ids.vstup.text = "0" #automaticky to zmeni vstup na nulu
```
- Úkol 6: Vytvořte funkci jednoho tlačítka, která slouží pro přepínání mezi nočním a denním režimem, po stisknutí budou tlačítka měnit svou barvu.

  app.py

```
class CalculatorWidget(Screen):
    temp_cislo = ""

    def zmen_rezim(self):
        for button_id in self.ids.keys():
            button = self.ids[button_id]
            if isinstance(button, Button):
                if button.background_color == [0, 1, 1, 1]:
                    button.background_color = [0.7, 0.7, 0.7, 1]
                else:
                    button.background_color = [0, 1, 1, 1]
```

- Celé řešení

app.py

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
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import NoTransition
from kivy.metrics import dp


from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.clock import Clock
from kivy.config import Config
from kivy.utils import platform
import math
from random import randint


Config.set('graphics', 'width', '1920')
Config.set('graphics', 'height', '1080')
#Builder.load_file("./my.kv") #loadnes file z root slozky
#Window.size = (350, 600) #velikost okna, sirka/vyska
#Config.set('graphics', 'resizable', False)
#Config.set('graphics', 'width', '350')
#Config.set('graphics', 'height', '600')

class CalculatorWidget(Screen):
    temp_cislo = ""

    def smaz(self):
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

        
class CalculatorManager(ScreenManager):
    pass

kv = Builder.load_file("./my.kv")

class MyApp(App):
    def build(self):
        if(platform == 'android' or platform == 'ios'):
            Window.maximize()
        #elif(Window.width == 1920 and Window.height == 1080):
        #    Window.size = (350 * (1920/2880), 600 * (1080/1800))
        else:
            Window.size = (350, 600)
        return kv


if __name__ == '__main__':
    MyApp().run()
```

my.kv 

```
<Button@Button>
    #background_normal: ''
    font_size: "16sp"

<TextBox@TextInput>
    font_size: "16sp"
    readonly: True
    multiline: False
    halign: "right" #odkud kam se zapisuje


CalculatorManager:
    CalculatorWidget:

<CalculatorWidget>:
    name: "prvni"

    BoxLayout: #-- sestaveniElementu
        orientation: "vertical"

        TextBox:
            id: vstup
            text: "0"
            size_hint_y: None
            height: 64
        
        TextBox:
            id: vystup
            text: ""
            font_size: "32sp"
            size_hint_y: None
            height: 128

        GridLayout: #udava pocet sloupcu, radku
            cols: 4
            rows: 6
            
            # Sloupec 1

            Button:
                id: rezim_button_1
                text: "AC"
                on_press: root.smaz()
                background_color: (0, 0, 0, 1)if root.ids.vstup.text == 'Error' else (0.7, 0.7, 0.7, 1)
            
            Button:
                id: rezim_button_2
                text: "C"
                on_press: root.vymaz_jedno()
                background_color: (0.7, 0.7, 0.7, 1)
            
            Button:
                #font_size: 32
                id: zmena_barvy
                on_press: root.zmen_rezim()
                background_normal: 'Day_night.jpeg'

            Button:
                background_normal: 'veda.jpg'
                id: prepnuti_kalkulacky
                #font_size: 32
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
                on_press: root.cisla(7) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_4
                text: "8"
                on_press: root.cisla(8) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_5
                text: "9"
                on_press: root.cisla(9) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_6
                text: "*"
                on_press: root.operace("*") 
                background_color: (0.7, 0.7, 0.7, 1)

            # SLOUPEC 3
            Button:
                id: rezim_button_7
                text: "4"
                on_press: root.cisla(4) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_8
                text: "5"
                on_press: root.cisla(5) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_9
                text: "6"
                on_press: root.cisla(6) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_10
                text: "-"
                on_press: root.operace("-")
                background_color: (0.7, 0.7, 0.7, 1)

            # SLOUPEC 4
            Button:
                id: rezim_button_11
                text: "1"
                on_press: root.cisla(1) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_12
                text: "2"
                on_press: root.cisla(2) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_13
                text: "3"
                on_press: root.cisla(3) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)


            Button:
                id: rezim_button_14
                text: "+"
                #font_size: 32
                on_press: root.operace("+") 
                background_color: (0.7, 0.7, 0.7, 1)

            # SLOUPEC 5
            
            Button:
                id: rezim_button_15
                text: "."
                #font_size: 32
                on_press: root.operace(".")
                background_color: (0.7, 0.7, 0.7, 1)
            Button:
                id: rezim_button_16
                text: "0"
                #font_size: 32
                on_press: root.cisla(0)
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)
            

            Button:
                id: rezim_button_17
                text: "="
                #font_size: 32
                on_press: root.vypocitej()
                background_color: (0.7, 0.7, 0.7, 1)
            

            Button:
                id: rezim_button_18
                text: "/"
                #font_size: 32
                on_press: root.operace("/")
                background_color: (0.7, 0.7, 0.7, 1)
```

  

  
- Úkol 7: Vytvořte grafické uživatelské rozhraní vědecké kalkulačky. Přidejte další tlačitka pro speciální matemetické funkce jako je mocnina, odmocnina, logaritmus, ... 

  ![image](https://github.com/NgocHuyVu/Kivy/assets/128366057/77f7e1b9-e599-420a-af7d-0a1c86cab7a9)

```

<ScienceCalculatorWidget>:
    name: "druhy"

    BoxLayout:
        id: sestaveniElementu
        orientation: "vertical"
        #orientation: "horizontal" pozdeji jeste prepsat 
        size: root.width, root.height

        TextBox:
            id: vstup
            text: "0"
            size_hint_y: None
            height: 64
        
        TextBox:
            id: vystup
            text: ""
            font_size: "32sp"
            size_hint_y: None
            height: 128

        GridLayout: #udava pocet sloupcu, radku
            cols: 4
            rows: 7

            # Sloupec 1

            Button:
                id: rezim_button_1
                text: "AC"
                on_press: root.smaz()
                background_color: (0, 0, 0, 1)if root.ids.vstup.text == 'Error' else (0.7, 0.7, 0.7, 1)
            
            Button:
                id: rezim_button_2
                text: "C"
                on_press: root.vymaz_jedno()
                background_color: (0.7, 0.7, 0.7, 1)
            
            Button:
                on_press: root.zmen_rezim()
                background_normal: 'Day_night.jpeg'

            Button:
                background_normal: 'veda.jpg'
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
                #font_size: 32
                on_press: root.jeden_deli_x() if not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else (0, 0, 0, 1)

            Button:
                id: rezim_button_4
                text: "x^2"
                #font_size: 32
                on_press: root.druha_mocnina() if not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else (0, 0, 0, 1)

            Button:
                id: rezim_button_5
                text: "x^3"
                #font_size: 32
                on_press: root.treti_mocnina() if not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else (0, 0, 0, 1)

            Button:
                id: rezim_button_6
                text: "√"
                #font_size: 32
                on_press: root.druha_odmocnina() if not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else (0, 0, 0, 1)


            # SLOUPEC 3
            Button:
                id: rezim_button_7
                text: "10^x"
                #font_size: 32
                on_press: root.umocnovani_desitkou() if not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else (0, 0, 0, 1)

            Button:
                id: rezim_button_8
                text: "π" #PI
                #font_size: 32
                on_press: root.pi() if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_9
                text: "log"
                #font_size: 32
                on_press: root.logaritmus_o_zakladu_10() if not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else (0, 0, 0, 1)

            Button:
                id: rezim_button_10
                text: "ln"
                #font_size: 32
                on_press: root.prirozeny_logaritmus() if not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else (0, 0, 0, 1)

            # SLOUPEC 3
            Button:
                id: rezim_button_11
                text: "7"
                #font_size: 32
                on_press: root.cisla(7) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_12
                text: "8"
                #font_size: 32
                on_press: root.cisla(8) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_13
                text: "9"
                #font_size: 32
                on_press: root.cisla(9) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_14
                text: "*"
                #font_size: 32
                on_press: root.operace("*") 
                background_color: (0.7, 0.7, 0.7, 1)

            # SLOUPEC 4
            Button:
                id: rezim_button_15
                text: "4"
                on_press: root.cisla(4) if root.ids.vstup.text[-1] not in ('=') else None
                #font_size: 32
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_16
                text: "5"
                #font_size: 32
                on_press: root.cisla(5) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_17
                text: "6"
                #font_size: 32
                on_press: root.cisla(6) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_18
                text: "-"
                #font_size: 32
                on_press: root.operace("-")
                background_color: (0.7, 0.7, 0.7, 1)

            # SLOUPEC 5
            Button:
                id: rezim_button_19
                text: "1"
                #font_size: 32
                on_press: root.cisla(1) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_20
                text: "2"
                #font_size: 32
                on_press: root.cisla(2) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_21
                text: "3"
                #font_size: 32
                on_press: root.cisla(3) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)


            Button:
                id: rezim_button_22
                text: "+"
                #font_size: 32
                on_press: root.operace("+") 
                background_color: (0.7, 0.7, 0.7, 1)

            # SLOUPEC 6
            
            Button:
                id: rezim_button_23
                text: "."
                on_press: root.operace(".")
                #font_size: 32
                background_color: (0.7, 0.7, 0.7, 1)
            Button:
                id: rezim_button_24
                text: "0"
                #font_size: 32
                on_press: root.cisla(0)
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)
            

            Button:
                id: rezim_button_25
                text: "="
                #font_size: 32
                on_press: root.vypocitej()
                background_color: (0.7, 0.7, 0.7, 1)
            Button:
                id: rezim_button_26
                text: "/"
                #font_size: 32
                on_press: root.operace("/")
                background_color: (0.7, 0.7, 0.7, 1)
```

- Úkol 8: Vytvoření funkce tlačítka, která slouží pro navigaci mezi základní kalkulačkou a vědeckou kalkulačkou.

  app.py
  
```
class CalculatorWidget(Screen):
   ...
    
    def vedecka_kalkulacka_velikost(self):
        Window.size = (700,400)

class ScienceCalculatorWidget(Screen):
    ...
    
    def vedecka_kalkulacka_velikost(self):
        Window.size = (350,600)
```

my.kv
```

	Button:
                background_normal: 'veda.jpg'
                id: prepnuti_kalkulacky
                #font_size: 32
                #on_press: root.vedecka_kalkulacka_velikost()  
                #on_press: root.current = 'sc_kalkulacka'
                on_release: 
                    root.vedecka_kalkulacka_velikost()  
                    app.root.current = "druhy"
                    root.manager.transition.direction = "left"
```

  
- Úkol 8: Implementace funkcí tlačítka 

- Celé řešení
 app.py

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
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import NoTransition
from kivy.metrics import dp
import math
from random import randint
from kivy.config import Config
from kivy.utils import platform


from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.clock import Clock


class CalculatorWidget(Screen):
    temp_cislo = ""

    def smaz(self):
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
            self.ids.vstup.text += str(math.pi)
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
    temp_cislo = ""

    def smaz(self):
        self.ids.vstup.text = "0"
        self.ids.vystup.text = ""
        CalculatorWidget.temp_cislo = ""

    def vymaz_jedno(self):
        if len(self.ids.vstup.text) > 1:
            self.ids.vstup.text = self.ids.vstup.text[:-1]
        else:
            self.ids.vstup.text = "0"
    def jeden_deli_x(self):
        vstup_cisla = self.ids.vstup.text
        if float(vstup_cisla) == 0:
            self.ids.vstup.text = "Error"
        else: 
            self.ids.vstup.text = str(1 / float(vstup_cisla))
    def druha_mocnina(self):
        vstup_cisla = self.ids.vstup.text
        self.ids.vstup.text = str(float(vstup_cisla) ** 2)

    def treti_mocnina(self):
        vstup_cisla = self.ids.vstup.text
        self.ids.vstup.text = str(float(vstup_cisla) ** 3)

    def druha_odmocnina(self):
        vstup_cisla = self.ids.vstup.text
        if float(vstup_cisla) <= 0:
            self.ids.vstup.text = "Error"
        else:
            self.ids.vstup.text = str(float(vstup_cisla) ** 0.5)

    def umocnovani_desitkou(self):
        vstup_cisla = self.ids.vstup.text
        self.ids.vstup.text = str(10 ** float(vstup_cisla))

    def logaritmus_o_zakladu_10(self):
        vstup_cisla = self.ids.vstup.text
        if float(vstup_cisla) <= 0:
            self.ids.vstup.text = "Error"
        else:
            self.ids.vstup.text = str(math.log10(float(vstup_cisla)))

    def prirozeny_logaritmus(self):
        vstup_cisla = self.ids.vstup.text
        if float(vstup_cisla) <= 0:
            self.ids.vstup.text = "Error"
        else:
            self.ids.vstup.text = str(math.log(float(vstup_cisla)))

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
    def pi(self):
        vstup_cisla = self.ids.vstup.text
        pi_num = math.pi

        if vstup_cisla == "0":
            self.ids.vstup.text = str(pi_num)
        else:
            self.ids.vstup.text  = (f"{vstup_cisla}{pi_num}")
        vstup_cisla = self.ids.vstup.text
        
    def vypocitej(self):
        vstup = self.ids.vstup.text
        try:
            self.ids.vystup.text = str(eval(vstup))
            self.ids.vstup.text  = self.ids.vstup.text + "="
            CalculatorWidget.temp_cislo = self.ids.vystup.text
            
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


class CalculatorManager(ScreenManager):
    pass

kv = Builder.load_file("./my.kv")

class MyApp(App):
    def build(self):
        if(platform == 'android' or platform == 'ios'):
            Window.maximize()
        #elif(Window.width == 1920 and Window.height == 1080):
        #    Window.size = (350 * (1920/2880), 600 * (1080/1800))
        else:
            Window.size = (350, 600)
        return kv


if __name__ == '__main__':
    MyApp().run() 
```
my.kv

```
<Button@Button>
    #background_normal: ''
    font_size: "16sp"

<TextBox@TextInput>
    font_size: "16sp"
    readonly: True
    multiline: False
    halign: "right" #odkud kam se zapisuje


CalculatorManager:
    CalculatorWidget:
    ScienceCalculatorWidget:

<CalculatorWidget>:
    name: "prvni"

    BoxLayout: #-- sestaveniElementu
        orientation: "vertical"

        TextBox:
            id: vstup
            text: "0"
            size_hint_y: None
            height: 64
        
        TextBox:
            id: vystup
            text: ""
            font_size: "32sp"
            size_hint_y: None
            height: 128

        GridLayout: #udava pocet sloupcu, radku
            cols: 4
            rows: 6
            
            # Sloupec 1

            Button:
                id: rezim_button_1
                text: "AC"
                on_press: root.smaz()
                background_color: (0, 0, 0, 1)if root.ids.vstup.text == 'Error' else (0.7, 0.7, 0.7, 1)
            
            Button:
                id: rezim_button_2
                text: "C"
                on_press: root.vymaz_jedno()
                background_color: (0.7, 0.7, 0.7, 1)
            
            Button:
                #font_size: 32
                id: zmena_barvy
                on_press: root.zmen_rezim()
                background_normal: 'Day_night.jpeg'

            Button:
                background_normal: 'veda.jpg'
                id: prepnuti_kalkulacky
                #font_size: 32
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
                on_press: root.cisla(7) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_4
                text: "8"
                on_press: root.cisla(8) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_5
                text: "9"
                on_press: root.cisla(9) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_6
                text: "*"
                on_press: root.operace("*") 
                background_color: (0.7, 0.7, 0.7, 1)

            # SLOUPEC 3
            Button:
                id: rezim_button_7
                text: "4"
                on_press: root.cisla(4) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_8
                text: "5"
                on_press: root.cisla(5) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_9
                text: "6"
                on_press: root.cisla(6) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_10
                text: "-"
                on_press: root.operace("-")
                background_color: (0.7, 0.7, 0.7, 1)

            # SLOUPEC 4
            Button:
                id: rezim_button_11
                text: "1"
                on_press: root.cisla(1) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_12
                text: "2"
                on_press: root.cisla(2) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_13
                text: "3"
                on_press: root.cisla(3) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)


            Button:
                id: rezim_button_14
                text: "+"
                #font_size: 32
                on_press: root.operace("+") 
                background_color: (0.7, 0.7, 0.7, 1)

            # SLOUPEC 5
            
            Button:
                id: rezim_button_15
                text: "."
                #font_size: 32
                on_press: root.operace(".")
                background_color: (0.7, 0.7, 0.7, 1)
            Button:
                id: rezim_button_16
                text: "0"
                #font_size: 32
                on_press: root.cisla(0)
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)
            

            Button:
                id: rezim_button_17
                text: "="
                #font_size: 32
                on_press: root.vypocitej()
                background_color: (0.7, 0.7, 0.7, 1)
            

            Button:
                id: rezim_button_18
                text: "/"
                #font_size: 32
                on_press: root.operace("/")
                background_color: (0.7, 0.7, 0.7, 1)
            
        Button:
            id: rezim_button_19
            text: "had"
            #font_size: 32
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
        id: sestaveniElementu
        orientation: "vertical"
        #orientation: "horizontal" pozdeji jeste prepsat 
        size: root.width, root.height

        TextBox:
            id: vstup
            text: "0"
            size_hint_y: None
            height: 64
        
        TextBox:
            id: vystup
            text: ""
            font_size: "32sp"
            size_hint_y: None
            height: 128

        GridLayout: #udava pocet sloupcu, radku
            cols: 4
            rows: 7

            # Sloupec 1

            Button:
                id: rezim_button_1
                text: "AC"
                on_press: root.smaz()
                background_color: (0, 0, 0, 1)if root.ids.vstup.text == 'Error' else (0.7, 0.7, 0.7, 1)
            
            Button:
                id: rezim_button_2
                text: "C"
                on_press: root.vymaz_jedno()
                background_color: (0.7, 0.7, 0.7, 1)
            
            Button:
                on_press: root.zmen_rezim()
                background_normal: 'Day_night.jpeg'

            Button:
                background_normal: 'veda.jpg'
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
                #font_size: 32
                on_press: root.jeden_deli_x() if not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else (0, 0, 0, 1)

            Button:
                id: rezim_button_4
                text: "x^2"
                #font_size: 32
                on_press: root.druha_mocnina() if not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else (0, 0, 0, 1)

            Button:
                id: rezim_button_5
                text: "x^3"
                #font_size: 32
                on_press: root.treti_mocnina() if not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else (0, 0, 0, 1)

            Button:
                id: rezim_button_6
                text: "√"
                #font_size: 32
                on_press: root.druha_odmocnina() if not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else (0, 0, 0, 1)


            # SLOUPEC 3
            Button:
                id: rezim_button_7
                text: "10^x"
                #font_size: 32
                on_press: root.umocnovani_desitkou() if not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else (0, 0, 0, 1)

            Button:
                id: rezim_button_8
                text: "π" #PI
                #font_size: 32
                on_press: root.pi() if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_9
                text: "log"
                #font_size: 32
                on_press: root.logaritmus_o_zakladu_10() if not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else (0, 0, 0, 1)

            Button:
                id: rezim_button_10
                text: "ln"
                #font_size: 32
                on_press: root.prirozeny_logaritmus() if not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and not any(op in root.ids.vstup.text for op in ('/', '*', '-', '+', '=')) else (0, 0, 0, 1)

            # SLOUPEC 3
            Button:
                id: rezim_button_11
                text: "7"
                #font_size: 32
                on_press: root.cisla(7) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_12
                text: "8"
                #font_size: 32
                on_press: root.cisla(8) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_13
                text: "9"
                #font_size: 32
                on_press: root.cisla(9) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_14
                text: "*"
                #font_size: 32
                on_press: root.operace("*") 
                background_color: (0.7, 0.7, 0.7, 1)

            # SLOUPEC 4
            Button:
                id: rezim_button_15
                text: "4"
                on_press: root.cisla(4) if root.ids.vstup.text[-1] not in ('=') else None
                #font_size: 32
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_16
                text: "5"
                #font_size: 32
                on_press: root.cisla(5) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_17
                text: "6"
                #font_size: 32
                on_press: root.cisla(6) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_18
                text: "-"
                #font_size: 32
                on_press: root.operace("-")
                background_color: (0.7, 0.7, 0.7, 1)

            # SLOUPEC 5
            Button:
                id: rezim_button_19
                text: "1"
                #font_size: 32
                on_press: root.cisla(1) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_20
                text: "2"
                #font_size: 32
                on_press: root.cisla(2) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)

            Button:
                id: rezim_button_21
                text: "3"
                #font_size: 32
                on_press: root.cisla(3) if root.ids.vstup.text[-1] not in ('=') else None
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)


            Button:
                id: rezim_button_22
                text: "+"
                #font_size: 32
                on_press: root.operace("+") 
                background_color: (0.7, 0.7, 0.7, 1)

            # SLOUPEC 6
            
            Button:
                id: rezim_button_23
                text: "."
                on_press: root.operace(".")
                #font_size: 32
                background_color: (0.7, 0.7, 0.7, 1)
            Button:
                id: rezim_button_24
                text: "0"
                #font_size: 32
                on_press: root.cisla(0)
                background_color: (0.7, 0.7, 0.7, 1) if root.ids.vstup.text and root.ids.vstup.text[-1] != '=' else (0, 0, 0, 1)
            

            Button:
                id: rezim_button_25
                text: "="
                #font_size: 32
                on_press: root.vypocitej()
                background_color: (0.7, 0.7, 0.7, 1)
            Button:
                id: rezim_button_26
                text: "/"
                #font_size: 32
                on_press: root.operace("/")
                background_color: (0.7, 0.7, 0.7, 1)
```
