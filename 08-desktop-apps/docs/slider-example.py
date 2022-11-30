from kivy.app import App
from kivy.uix.slider import Slider
from kivy.uix.anchorlayout import AnchorLayout


class MainApp(App):

    def build(self):
        root = AnchorLayout(anchor_x='center', anchor_y='center')
        root.add_widget(
            Slider(
                min=0,
                max=100,
                value=25,
                step=1,
                size_hint=(None, None),
                size=(250, 32),
            )
        )
        return root


if __name__ == '__main__':
    app = MainApp(title="Ejemplo de slider")
    app.run()
