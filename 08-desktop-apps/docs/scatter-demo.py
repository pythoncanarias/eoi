from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout


class ScatterDemoApp(App):

    def build(self):
        f = FloatLayout()
        s = Scatter()
        l1 = Label(text='Hola', font_size=150)
        l2 = Label(text='Mundo!', font_size=150)
        f.add_widget(s)
        s.add_widget(l1)
        s.add_widget(l2)
        return f

def main():
    app = ScatterDemoApp()
    app.run()

if __name__ == '__main__':
    main()