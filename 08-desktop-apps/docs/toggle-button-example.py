from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.togglebutton import ToggleButton


class MainApp(App):

    def switch_booster(self, instance):
        if instance.state == 'down':
            instance.text = 'Boost enabled'
        else:
            instance.text = 'Boost disabled'

    def build(self):
        root = AnchorLayout(anchor_x='center', anchor_y='center')
        pb_boost = ToggleButton(
                text='Boost disabled',
                state='normal',
                size_hint=(None, None),
                size=(150, 48),
            )
        pb_boost.bind(on_press=self.switch_booster)
        root.add_widget(pb_boost)
        return root


if __name__ == '__main__':
    app = MainApp(title="Ejemplo de ToogleButton")
    app.run()
