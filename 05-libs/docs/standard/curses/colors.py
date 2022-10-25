#!/usr/bin/env python

import sys
import curses

def define_colors():
    curses.start_color()
    for i in range(1, 8):
        curses.init_pair(i, i, curses.COLOR_BLACK)


def main(stdscr):
    define_colors()
    stdscr.clear()
    msg = "{} ({} x {})".format(
        sys.argv[0],
        curses.COLS,
        curses.LINES,
        )
    x_pos = curses.COLS - len(msg) - 2
    stdscr.addstr(1, x_pos, msg, curses.A_BOLD)
    stdscr.border()

    for color in range(8):
        msg = "Texto en colos {}".format(color)
        stdscr.addstr(5+color, 4, msg, curses.color_pair(color))

    stdscr.refresh()

    stdscr.getkey()


if __name__ == "__main__":
    curses.wrapper(main)
