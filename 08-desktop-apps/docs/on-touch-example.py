from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button


class MyButton(Button):

    def on_touch_down(self, event):
        print(f'TOUCH DOWN x={event.x} y={event.y}')

    def on_touch_move(self, event):
        print(f'MOVE x={event.x} y={event.y}')

    def on_touch_up(self, event):
        print(f'TOUCH UP x={event.x} y={event.y}')


class MainApp(App):

    def build(self):
        root = Widget()
        root.add_widget(
            MyButton(
                text="boton",
                background_color=(1, 0, .2, 0.7),
                size=(450, 125),
                pos=(100, 100)
            )
        )
        return root
                

if __name__ == '__main__':
    app = MainApp(title="Ejemplo de eventos on_touch_*") 
    app.run()
