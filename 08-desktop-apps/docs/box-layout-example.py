from kivy.app import App
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.boxlayout import BoxLayout


class MainApp(App):

    def build(self):
        root = BoxLayout(padding=10, spacing=5)
        root.add_widget(ToggleButton(text="Edificio Baxter", group='hq'))
        root.add_widget(ToggleButton(text="Torre Vengadores", group='hq'))
        root.add_widget(ToggleButton(text="Escuela Xavier", group='hq'))
        return root


if __name__ == '__main__':
    app = MainApp(title="Ejemplo de BoxLayout")
    app.run()
