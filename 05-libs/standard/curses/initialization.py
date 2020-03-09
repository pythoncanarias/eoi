import curses


def main(stdscr):
    # Clear screen
    stdscr.clear()

    # ops, eleva ZeroDivisionError cuando i == 0.
    for i in range(0, 11):
        stdscr.addstr(i, 0, '10 / {} == {}'.format(i, 10/i))

    stdscr.refresh()
    stdscr.getkey()


if __name__ == "__main__":
    curses.wrapper(main)
