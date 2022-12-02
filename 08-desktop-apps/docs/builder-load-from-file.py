from kivy.app import App
from kivy.lang.builder import Builder


class LoadFromFile(App):

    def build(self):
        return Builder.load_file("builder.kv")


if __name__ == "__main__":
    app = LoadFromFile()
    app.run()
