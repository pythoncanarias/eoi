from kivy.app import App
from kivy.uix.textinput import TextInput


class CapitalInput(TextInput):

    def insert_text(self, substring, from_undo=False):
        s = substring.upper()
        return super().insert_text(s, from_undo=from_undo)


class TextInputCapitalExampleApp(App):

    def build(self):
        txt = CapitalInput(
            text="",
            multiline=True,
            font_size='16sp',
            background_color='#EFEFEF',
            )
        return txt


if __name__ == '__main__':
    app = TextInputCapitalExampleApp(title="Ejemplo TextInput (Capitals)")
    app.run()
