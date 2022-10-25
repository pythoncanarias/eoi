from kivy.app import App
from kivy.uix.button import Button

class MainApp(App):

    def build(self):
        self.btn = Button(
           text="Hello World",
           size_hint=(0.4,0.05),
           pos_hint={'x': 0.3, 'y': 0.5},
           background_color = "#FF0000",
           )
        return self.btn


def main():
    app = MainApp() 
    app.run()


if __name__ == '__main__':
    main()
