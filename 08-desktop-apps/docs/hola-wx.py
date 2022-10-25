#!/usr/bin/env python3

import wx

def main():
    app = wx.App ()
    ventana = wx.Frame(
        None,
        title = "wxPython : Hola, mundo",
        size = (300,200)
        )
    panel = wx.Panel(ventana) 
    button = wx.Button(panel, label="Hello World", pos = (100,50)) 
    ventana.Show(True)
    app.MainLoop()


if __name__ == '__main__':
    main()
