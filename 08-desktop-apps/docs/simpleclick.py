from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class MainLayout(BoxLayout):

    def click(self):
        print('Hola, mundo')


class SimpleClickApp(App):
    pass



if __name__ == '__main__':
    app = SimpleClickApp() 
    app.run()
