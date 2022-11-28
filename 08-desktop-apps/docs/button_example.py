from kivy.app import App
from kivy.uix.button import Button

POSITIONS = [
    {'x': 0.05, 'top': 0.95 },
    {'right': 0.95, 'top': 0.95 },
    {'right': 0.95, 'y': 0.05 },
    {'x': 0.05, 'y': 0.05 },
]

class ButtonExampleApp(App):

    def say_hello(self, widget):
        print("Hola, mundo")
        print(f"{widget=!r}")
        print(f"{widget.size=!r}")
        self.position_index = (self.position_index + 1) % len(POSITIONS)
        widget.pos_hint = POSITIONS[self.position_index]


    def build(self):
        self.position_index = 0
        button = Button(
            text="[u]Hola[/u], [b][color=ff3333]mundo[/color][/b]",
            markup=True,
            font_size=32,
            background_color='#CC33AA',
            # size_hint=(0.5, 0.5),
            size_hint=(None, None),
            size=(220, 64),
            pos_hint=POSITIONS[self.position_index],
            )
        button.bind(on_press=self.say_hello)
        return button


if __name__ == '__main__':
    app = ButtonExampleApp(title="Hola, mundo Kivy")
    app.run()
