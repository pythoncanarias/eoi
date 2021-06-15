from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
 
class GridLayoutApp(App):
    def build(self):
        grid = GridLayout()
        for y in range(8): 
            for x in range(8):
                if (x+y) % 2 == 0:
                    grid.add_widget(Button(text="white"))
                else:
                    grid.add_widget(Label(text="black"))
        return grid
 
if __name__=="__main__":
  app = GridLayoutApp()
  app.run()