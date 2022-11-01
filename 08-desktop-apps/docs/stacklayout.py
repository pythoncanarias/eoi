from kivy.app import App
from kivy.uix.stacklayout import StackLayout
 

class StackLayoutApp(App):
    def build(self):
        return StackLayout()
 
if __name__=="__main__":
  app = StackLayoutApp()
  app.run()