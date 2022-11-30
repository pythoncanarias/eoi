from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.widget import Widget


class MainApp(App):

    def build(self):
        root = Widget(size=(300, 300))
        root.add_widget(
            Button(
                text='A',
                pos=(0, 0),
                size=(80, 80),
            ))
        root.add_widget(
            Button(
                text='B',
                pos=(150-40, 150-40),
                size=(80, 80),
            ))
        root.add_widget(
            Button(
                text='C',
                pos=(300-80, 300-80),
                size=(80, 80),
            ))
        return root


if __name__ == '__main__':
    app = MainApp(title="Ejemplo de FloatLayout (Antes)")
    Window.size = (300, 300)
    app.run()
