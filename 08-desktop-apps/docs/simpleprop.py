from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty


class MainLayout(BoxLayout):

    message = StringProperty("Hola, mundo")

    def click(self):
        self.message = 'Click pulsado'


class SimplePropApp(App):
    pass


if __name__ == '__main__':
    app = SimplePropApp()
    app.run()
