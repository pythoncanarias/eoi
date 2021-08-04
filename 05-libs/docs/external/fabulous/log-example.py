#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time
import logging

from fabulous import logs

logs.basicConfig(level=logging.WARNING)

for n in range(20):
    logging.debug("verbose stuff you don't care about")
    time.sleep(0.1)
logging.warning("something bad happened!")
for n in range(20):
    logging.debug("verbose stuff you don't care about")
    time.sleep(0.1)
