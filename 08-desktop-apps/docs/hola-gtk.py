import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class PyApp(Gtk.Window):

    def __init__(self):
        super().__init__()
        self.set_default_size(300,200)
        self.set_title("PyGTK : Hola, mundo")
        button = Gtk.Button("Hello, World")
        button.set_alignment(0.5, 0.5)
        self.add(button)
        self.show_all()
           

def main():
    app = PyApp()
    Gtk.main()

if __name__ == '__main__':
    main()

