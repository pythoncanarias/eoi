from kivy.app import App
from kivy.uix.widget import Widget

class MainApp(App):

    def build(self):
        return Widget(
            background_color=(1, 0, 0, 1),
            )


if __name__ == '__main__':
    app = MainApp(title="instanciando un Widget") 
    app.run()
