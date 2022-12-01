import random

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.scatter import Scatter
from kivy.metrics import dp
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle


class Item(Scatter):
    def __init__(self, text, *args, **kwargs):
        super().__init__(*args, **kwargs)
        _color = (random.random(), random.random(), random.random())
        self.label = Label(text=text, font_size=dp(32), color=_color)
        self.add_widget(self.label)
        # self.canvas.add(Rectangle(size=self.label.size))


class ImageItem(Scatter):
    def __init__(self, filename, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = Label(text=filename)
        self.img = Image(source=filename)
        self.add_widget(self.img)
        self.add_widget(self.label)

# self.canvas.add(Rectangle(size=self.label.size))
class ScatterDemoApp(App):

    def build(self):
        f = FloatLayout()
        f.add_widget(Item("Hola"))
        f.add_widget(Item("Mundo"))
        f.add_widget(ImageItem("pictures/beast.png"))
        return f

    def on_pause(self):
        return True
    

def main():
    app = ScatterDemoApp()
    app.run()

if __name__ == '__main__':
    main()
