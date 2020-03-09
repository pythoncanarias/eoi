#!/usr/bin/env python

import sys
import curses


def main(stdscr):
    stdscr.clear()
    msg = "{} ({} x {})".format(
        sys.argv[0],
        curses.COLS,
        curses.LINES,
        )
    x_pos = curses.COLS - len(msg) - 2
    stdscr.addstr(1, x_pos, msg, curses.A_BOLD)
    stdscr.border()

    stdscr.addch(20, 2, 8730)
    stdscr.refresh()
    stdscr.getkey()


if __name__ == "__main__":
    curses.wrapper(main)
