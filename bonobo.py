import kivy
import NEWUSER
from kivy.uix.button import Button 
import loginsql
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.button import Button
Window.clearcolor = (.70, 0,0 , 0)
class Widgetx(Widget):
    def __init__(self, **kwargs):
        super(Widgetx, self).__init__(**kwargs)
    def print_off(self):
        self.login_string=self.ids.username.text
        self.login_verify=self.ids.passw.text
        loginsql.log_in(self.login_string,self.login_verify)
       
    def registerx_(self):
        self.ids.login_button.opacity=0
        self.ids.login_button.disabled=True
        self.ids.passw.opacity=0
        self.ids.passw.disabled=True
        self.ids.username.opacity=0
        self.ids.username.disabled=True
        self.ids.sex.opacity=1
        self.ids.sex.disabled=False
        self.ids.username_sign.opacity=1
        self.ids.username_sign.disabled=False
        self.ids.passw_.opacity=1
        self.ids.passw_.disabled=False
        self.ids.Zip.opacity=1
        self.ids.Zip.disabled=False
        self.ids.email_phone.opacity=1
        self.ids.email_phone.disabled=False
        self.ids.age.opacity=1
        self.ids.age.disabled=False
        self.ids.register.opacity=1
        self.ids.register.disabled=True
        self.ids.name.opacity=1
        self.ids.name.disabled=False
        self.ids.sign_up.opacity=1
        self.ids.sign_up.disabled=False
        #need to implement email phone
    def regsend(self):
        NEWUSER.connx(self.ids.username_sign.text,self.ids.passw_.text,self.ids.age.text,self.ids.sex.text,self.ids.name.text)
class bonobo(App):
   def build(self):
      return Widgetx()
if __name__=="__main__":
   bonobo().run()