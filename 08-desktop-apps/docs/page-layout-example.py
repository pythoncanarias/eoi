from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.button import Button


class PageLayoutExampleApp(App):

    def build(self):
        root = PageLayout()
        root.add_widget(Button(text='Página 1', font_size='72sp'))
        root.add_widget(Button(text='Página 2', font_size='72sp'))
        root.add_widget(Button(text='Página 3', font_size='72sp'))
        return root


if __name__ == '__main__':
    app = PageLayoutExampleApp(title='Ejemplo de PageLayout')
    app.run()
