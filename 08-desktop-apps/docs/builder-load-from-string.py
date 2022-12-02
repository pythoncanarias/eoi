from kivy.app import App
from kivy.lang.builder import Builder

KV_LAYOUT = '''
BoxLayout:
    orientation: 'vertical'
    Label:
        size_hint: (1, 12)
        Image:
            size: root.size
            source: 'pictures/beast.png'
            center_x: self.parent.center_x
            center_y: self.parent.center_y

    Button:
        size_hint: (1, 1)
        text: "Hello Beast!"
'''


class LoadFromStringExample(App):

    def build(self):
        return Builder.load_string(KV_LAYOUT)


if __name__ == '__main__':
    app = LoadFromStringExample(title='Ejemplo de PageLayout')
    app.run()
