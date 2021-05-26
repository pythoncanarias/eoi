#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("num", type=int, help="valor a elevar al cuadrado")
parser.add_argument(
        "--explicacion",
        help="Muestra los pasos previos",
        type=int,
        default=0,
        )

options = parser.parse_args()
if options.explicacion > 0:
    print(f"{options.num}^2 = {options.num**2}")
else:
    print(options.num**2)
