#!/usr/bin/env python

import sys
import curses


def update_all_windows(screen, *windows):
    screen.noutrefresh()
    for wins in windows:
        wins.noutrefresh()
    curses.doupdate()


def main(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    red = curses.color_pair(1)
    stdscr.clear()


    msg = "{} ({} x {})".format(
        sys.argv[0],
        curses.COLS,
        curses.LINES,
        )
    x_pos = curses.COLS - len(msg) - 2
    stdscr.addstr(1, x_pos, msg, red)
    stdscr.border()

    stdscr.hline(12, 0, '=', curses.COLS-1)

    w = curses.newwin(5, curses.COLS-10, 5, 5)
    w.border()

    pad = curses.newpad(100, 100)
    # These loops fill the pad with letters; addch() is
    # explained in the next section
    for y in range(0, 99):
        for x in range(0, 99):
            pad.addch(y, x, ord('a') + (x*x+y*y) % 26)

    # Displays a section of the pad in the middle of the screen.
    # (0,0) : coordinate of upper-left corner of pad area to display.
    # (5,5) : coordinate of upper-left corner of window area to be filled
    #         with pad content.
    # (20, 75) : coordinate of lower-right corner of window area to be
    #          : filled with pad content.
    stdscr.addch(20, 2, 8730)
    update_all_windows(stdscr, w)
    pad.refresh(0, 0, 5, 5, 20, 75)
    stdscr.getkey()


if __name__ == "__main__":
    curses.wrapper(main)
