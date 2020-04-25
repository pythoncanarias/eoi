#!/usr/bin/env python
# -*- coding: utf-8 -*-

import arrow

dia = arrow.get(2020, 1, 1)
while dia.year == 2020:
    if dia.day == 13 and dia.weekday() == 4:  # Es viernes y trece
        print(dia)
    dia = dia.shift(days=1)

