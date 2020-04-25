#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("target", help="texto a mostrar en la pantalla")
options = parser.parse_args()
print(options.target)

