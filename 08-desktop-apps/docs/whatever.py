import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class BoxLayoutExample(BoxLayout):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation = "vertical"
        # b1 = Button(text="First Button")
        # b2 = Button(text="Second button")
        # b3 = Button(text="Third button")
        # self.add_widget(b1)
        # self.add_widget(b2)
        # self.add_widget(b3)

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass


def main():
    app = TheLabApp()
    app.run()

if __name__ == "__main__":
    main()