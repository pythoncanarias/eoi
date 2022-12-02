#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from datetime import datetime, timedelta

import sched

scheduler = sched.scheduler(timefunc=time.time)  # (1)

def saytime():  # (2)
    print(time.ctime())
    scheduler.enter(10, priority=0, action=saytime)  # (3)

saytime()
try:
    scheduler.run(blocking=True)  # (4)
except KeyboardInterrupt:
    print('Stopped.')
