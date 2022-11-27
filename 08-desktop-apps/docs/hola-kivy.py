from kivy.app import App
from kivy.uix.button import Button

class MainApp(App):

    def build(self):
        return Button(text="Hello World")


if __name__ == '__main__':
    app = MainApp(title="Hola, mundo Kivy") 
    app.run()
