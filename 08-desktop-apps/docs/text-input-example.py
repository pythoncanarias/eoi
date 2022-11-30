from kivy.app import App
from kivy.uix.textinput import TextInput


class TextInputExampleApp(App):

    def build(self):
        txt = TextInput(
            text="Hola, mundo",
            multiline=True,
            font_size='16sp',
            background_color='#EFEFEF',
            )
        return txt


if __name__ == '__main__':
    app = TextInputExampleApp(title="Ejemplo TextInput")
    app.run()
