from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button


class MainApp(App):

    def boton_pulsado(self, instance):
        print("Botón pulsado")

    def estado_cambiado(self, instance, value):
        print(f"Estado del botón: {instance.state}")

    def build(self):
        button = Button(
                text='Botón',
                font_size='24sp',
                size_hint=(None, None),
                size=(128, 128),
                pos_hint={
                    'center_x': 0.5,
                    'center_y': 0.5,
                    },
                background_normal='./pictures/button-normal.png',
                background_down='./pictures/button-down.png',
            )
        button.bind(on_press=self.boton_pulsado)
        button.bind(state=self.estado_cambiado)
        return button


if __name__ == '__main__':
    app = MainApp(title="Ejemplo de Button")
    app.run()
