from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty

class WidgetExample(GridLayout):

    label_text = StringProperty("Hola, mundo")
    counter = 0

    def show_slider(self, widget):
        print(widget.value)

    def show_active(self, widget):
        print(widget.active)

    def ver_estado(self, widget):
        if widget.state == 'down':
            widget.text = "ON"        
            self.ids['count_button'].disabled = False
        else:
            widget.text = "OFF"
            self.ids['count_button'].disabled = True

    def print_hola(self):
        self.counter += 1
        self.label_text = f"Pulsado {self.counter} veces"

    def cambio_texto(self, widget):
        print(widget.text)

class ControlesApp(App):
    pass


def main():
    app = ControlesApp()
    app.run()


if __name__ == '__main__':
    main()
