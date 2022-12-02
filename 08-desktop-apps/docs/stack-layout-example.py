from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout


class MainApp(App):

    def build(self):
        root = StackLayout(orientation='lr-tb', padding=10, spacing=4)
        for n in range(24):
            root.add_widget(Button(
                text=str(n),
                width=110,
                height=32,
                size_hint=(None, None),
                ))
        return root


if __name__ == '__main__':
    app = MainApp(title="Ejemplo de StackLayout")
    app.run()
