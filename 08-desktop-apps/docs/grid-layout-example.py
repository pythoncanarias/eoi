from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class MainApp(App):

    def build(self):
        root = GridLayout(cols=3, padding=10, spacing=4)
        for n in range(9):
            root.add_widget(Button(text=str(n)))
        return root


if __name__ == '__main__':
    app = MainApp(title="Ejemplo de GridLayout")
    app.run()
