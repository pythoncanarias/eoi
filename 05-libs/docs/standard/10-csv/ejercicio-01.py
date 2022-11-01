#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

csv.register_dialect('marvel', delimiter=',', quoting=csv.QUOTE_NONE, escapechar="\\")
filename = "marvel-wikia-data.csv"
with open(filename, 'r') as f:
    reader = csv.reader(f, dialect="marvel")
    next(reader)  # Ignorar la primera linea
    for i, row in enumerate(reader):
        year = int(row[-1] if row[-1] else 0)
        if 1972 <= year <= 1974:
            print(row[1], year)
        if i == 24:
            break



