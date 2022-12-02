#!/usr/bin/env python
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.animation import Animation


class MainLayout(RelativeLayout):

    def move_it(self):
        pos_hint = {
            'center_x': 0.85,
            'center_y': 0.85,
            }
        anim = Animation(pos_hint=pos_hint)
        pb_move = self.ids.pb_move
        anim.start(pb_move)


class SimpleAnimationApp(App):
    pass


if __name__ == "__main__":
    app = SimpleAnimationApp()
    app.run()
