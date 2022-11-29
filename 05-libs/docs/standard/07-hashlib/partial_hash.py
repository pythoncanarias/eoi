#!/usr/bin/env python
# -*- coding: utf-8 -*-

from hashlib import md5

m = md5("Su teoría es descabellada".encode("utf-8"))
print("hash parcial:", m)
m.update(", pero no lo suficente para ser correcta.".encode("utf-8"))
print("hash final:", m)
