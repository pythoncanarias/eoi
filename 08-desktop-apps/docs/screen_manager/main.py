#!/usr/bin/env python
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string("""
<MenuScreen>:
    FloatLayout:
        Button:
            text: 'First Screen'
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = 'settings'
            pos_hint: {'right': 1, 'center_y': 0.5}
            size_hint: (None, None)
            size: ("196dp", "24dp")

<SettingsScreen>:
    FloatLayout:
        Button:
            text: 'Second Screen'
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'menu'
            pos_hint: {'x': 0, 'center_y': 0.5}
            size_hint: (None, None)
            size: ("196dp", "24dp")

""")

# Declare both screens
class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class ScreenManagerApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))
        return sm


def main():
    app = ScreenManagerApp()
    app.run()


if __name__ == '__main__':
    main()
