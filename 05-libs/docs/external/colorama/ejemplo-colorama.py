#!/usr/bin/env python
# -*- coding: utf-8 -*-


from colorama import init, Fore, Back, Style


def main():
    init(autoreset=True)
    messages = [
        'blah blah blah',
        (Fore.LIGHTYELLOW_EX + Style.BRIGHT
            + Back.MAGENTA + 'Alert!!!'),
        'blah blah blah'
    ]
    for m in messages:
        print(m)


if __name__ == "__main__":
    main()
