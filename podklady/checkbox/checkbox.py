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
