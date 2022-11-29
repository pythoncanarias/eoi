#!/usr/bin.env python3

from tkinter import Tk
from tkinter.ttk import Button


def main():
    root = Tk()
    label = Button(root, text="Hola, TKInter")
    label.pack(expand=1)
    root.geometry('350x200')
    root.mainloop()


if __name__ == '__main__':
    main()
