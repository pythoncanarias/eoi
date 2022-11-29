from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button


class MainApp(App):

    def build(self):
        root = Widget()
        root.add_widget(
            Label(
                text="Etiqueta",
            )
        )
        root.add_widget(
            Button(
                text="boton",
                background_color=(1, 0, 0, 1),
                size=(333, 25),
            )
        )
        print(root.children)
        return root
                

if __name__ == '__main__':
    app = MainApp(title="instanciando un Widget") 
    app.run()
