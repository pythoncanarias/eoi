from kivy.app import App
from kivy.uix.recycleview import RecycleView

class ExampleRV(RecycleView):

    def __init__(self, **kwargs):
        super(ExampleRV, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in range(20)]


class RecycleApp(App):
    
    def build(self):
        return ExampleRV()


def main():
    app = RecycleApp()
    app.run()


if __name__ == '__main__':
    main()