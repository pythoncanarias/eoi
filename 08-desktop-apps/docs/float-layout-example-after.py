from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout


class MainApp(App):

    def build(self):
        root = FloatLayout(size=(300, 300))
        root.add_widget(
            Button(
                text='A',
                pos_hint={
                    'x': 0,
                    'y': 0,
                },
                size_hint=(80/300, 80/300),
            ))
        root.add_widget(
            Button(
                text='B',
                pos_hint={
                    'center_x': 0.5,
                    'center_y': 0.5,
                },
                size_hint=(80/300, 80/300),
            ))
        root.add_widget(
            Button(
                text='C',
                pos_hint={
                    'top': 1,
                    'right': 1,
                },
                size_hint=(80/300, 80/300),
            ))
        return root


if __name__ == '__main__':
    app = MainApp(title="Ejemplo de FloatLayout (Después)")
    Window.size = (300, 300)
    app.run()
