from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout


class FloatExampleApp(App):

    def build(self):
        return FloatLayout()


if __name__ == '__main__':
    app = FloatExampleApp(title="Ejemplo de FloatLayout (kvlang)")
    Window.size = (300, 300)
    app.run()
