from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.core.window import Window
import os




class ButtonPressApp(App):
   def __init__(self):
      super(ButtonPressApp, self).__init__()
      self.btn1 = Button(size_hint =(.5, .5),
					pos_hint ={'center_x':.25, 'center_y':.75},
					text ="1")
      self.btn2 = Button(size_hint =(.5, .5),
					pos_hint ={'center_x':.75, 'center_y':.75},
					text ="2")
      self.btn3 = Button(size_hint =(.5, .5),
					pos_hint ={'center_x':.25, 'center_y':.25},
					text ="3")
      self.btn4 = Button(size_hint =(.5, .5),
					pos_hint ={'center_x':.75, 'center_y':.25},
					text ="4")

   def build(self):
      self.btn1.bind(on_press=self.authenticate)
      self.btn2.bind(on_press=self.authenticate)
      self.btn3.bind(on_press=self.authenticate)
      self.btn4.bind(on_press=self.authenticate)

      layout = RelativeLayout()
      layout.orientation = 'horizontal'
      layout.add_widget(self.btn1)
      layout.add_widget(self.btn2)
      layout.add_widget(self.btn3)
      layout.add_widget(self.btn4)

      return layout
   def authenticate(self, obj):
      #self.btn1.background_normal=''
      #self.btn1.color=(1,0,0,0.8)
      #self.btn1.text = 'Button Pressed'
      print("click")
      os.system('python3 EnterNFC.py')

MainLayout = ButtonPressApp()
MainLayout.fullscreen = True
MainLayout.run()