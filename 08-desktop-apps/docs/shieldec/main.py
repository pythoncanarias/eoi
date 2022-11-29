from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


def cifra(s, clave=3):
    buff = []
    for c in s:
        num = ord(c)
        if 65 <= num < 91:
            new_num = ((num - 65 + clave) % 26) + 65
            buff.append(str(chr(new_num)))
        elif 97 <= num < 123:
            new_num = ((num - 97 + clave) % 26) + 97
            buff.append(str(chr(new_num)))
        else:
            buff.append(c)
    return ''.join(buff)


class MainLayout(BoxLayout):

    def do_cifra(self):
        fuente = self.txt_input.text
        clave = int(self.keycode.value) 
        cifrado = cifra(fuente, clave)
        self.txt_output.text = cifrado
        print(cifrado)


class ShieldecApp(App):
    
    def build(self):
        self.root.txt_input = self.root.ids['txt_input']
        self.root.keycode = self.root.ids['keycode']
        self.root.txt_output = self.root.ids['txt_output']


def main():
    app = ShieldecApp()
    app.run()


if __name__ == '__main__':
    main()
