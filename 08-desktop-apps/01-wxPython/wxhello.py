#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx


def main():
    app = wx.App(False)
    frame = wx.Frame(None, wx.ID_ANY, "Hello World")
    frame.Show(True)
    app.MainLoop()


if __name__ == "__main__":
    main()
