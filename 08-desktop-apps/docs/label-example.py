from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label


class MainApp(App):

    def build(self):
        root = Widget()
        root.add_widget(
            Label(
                text="[color=#ff2233]Hola[/color], [u]mundo[/u]",
                markup=True,
                font_size="22",
                pos=(200, 200),
                text_size=(150, 40),
            )
        )
        return root
                

if __name__ == '__main__':
    app = MainApp(title="Ejemplo de etiqueta") 
    app.run()
