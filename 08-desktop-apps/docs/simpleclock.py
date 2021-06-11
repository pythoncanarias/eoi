#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock

import datetime

class LabelClock(Label):
    pass


class SimpleClockApp(App):

    def on_start(self):
        Clock.schedule_interval(self.update, 1)

    def update(self, *args):
        now = datetime.datetime.now()
        hh, mm, ss = now.hour, now.minute, now.second
        self.root.ids.lbl_clock.text = f"{hh:02d}:{mm:02d}:{ss:02d}"


def main():
    app = SimpleClockApp()
    app.run()


if __name__ == "__main__":
    main()
