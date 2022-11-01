from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder


class BuilderDemo(App):

    def build(self):
        print("builder stars")
        # return Builder.load_string("""
# Button:
    # text: "Hello Button!"
    # Image:
        # source: 'img/angel.png'
        # center_x: self.parent.center_x
        # center_y: self.parent.center_y
# """)
        return Builder.load_file("builder.kv")

def main():
    app = BuilderDemo()
    app.run()


if __name__ == "__main__":
    main()
