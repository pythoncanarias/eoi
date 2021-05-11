#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def simula_tornillo():
    MEDIA = 10.0
    SIGMA = 0.0245
    return random.gauss(MEDIA, SIGMA)

for i in range(10):
    print(simula_tornillo())
