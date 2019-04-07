#2018 Zach Boyle
import kivy
from kivy.app import App
import chatclient
from chatclient import *
from kivy.properties import StringProperty
import time
import _thread
import threading
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.button import Button
Window.clearcolor = (0, 20, 0, 0)
global board_label
message_q=[]
class Widgetx(Widget):
    board_var=StringProperty('')
    def __init__(self, **kwargs):
        super(Widgetx, self).__init__(**kwargs)
    def get_inputer(self):
       chatclient.sender(self.ids.user_input.text)
def board_update(input):
   App.get_running_app().root.ids.input_board.text=input
class chat(App):
   def build(self):
      return Widgetx()
if __name__=="__main__":
   chat().run()
