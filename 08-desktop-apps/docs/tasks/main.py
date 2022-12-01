#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty

class MainLayout(BoxLayout):

    orden = NumericProperty(50)


class TaskMasterApp(App):
    pass


if __name__ == "__main__":
    app = TaskMasterApp()
    app.run()

