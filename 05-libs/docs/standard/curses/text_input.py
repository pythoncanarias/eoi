#!/usr/bin/env python

import sys
import curses
from curses.textpad import Textbox, rectangle

def main(stdscr):
    stdscr.addstr(0, 0, "Introduzca mensaje: (Ctrl-G para terminar)")

    editwin = curses.newwin(5, 30, 2,1)
    rectangle(stdscr, 1,0, 1 + 5 + 1, 1 + 30 +1)
    stdscr.refresh()

    box = Textbox(editwin)
    box.edit()  # Let the user edit until Ctrl-G is struck
    message = box.gather()  # Get resulting contents


if __name__ == "__main__":
    curses.wrapper(main)
