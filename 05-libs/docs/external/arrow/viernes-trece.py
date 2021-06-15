#!/usr/bin/env python
# -*- coding: utf-8 -*-

import arrow

year = 2021
for month in range(1, 13):
    day13 = arrow.get(day=13, month=month, year=year)
    if day13.isoweekday() == 4:
        print(day13)

