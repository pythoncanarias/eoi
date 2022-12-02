#!/usr/bin/env python

import kivy

from kivy.app import App
from kivy.uix.togglebutton import ToggleButton

#our class to create a button and execute it
class ButtonApp(App):

    def build(self):
        return ToggleButton(
            pos_hint={
                'center_x': 0.5,
                'center_y': 0.5,
                },
            size_hint=(None, None),
            size=(256, 256),
            background_normal='pictures/boost_off.png',
            background_down='pictures/boost_on.png',
            )


if __name__ == "__main__":
    app = ButtonApp(title="Ejemplo fondo en botones")
    app.run()
