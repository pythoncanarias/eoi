#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import datetime

import sched

def backup(ruta):  # (1)
    """Funcion de backup simulada.
    """
    now = datetime.datetime.now()
    hhmmss = f"{now.hour:02d}:{now.minute:02d}:{now.second:02d}"
    print(f"{hhmmss} Empiezo backup {ruta}", end=": ", flush=True)
    for _ in range(7):
        time.sleep(1)
        print(".", end="", flush=True)
    print("Terminado", end=" [OK]\n", flush=True)


scheduler = sched.scheduler(timefunc=time.time)  # (2)
today = datetime.date.today()  # (3)
year, month, day = today.year, today.month, today.day

t_first_backup = datetime.datetime(year, month, day, 17, 37, 0)  # (4)
scheduler.enterabs(
    t_first_backup.timestamp(),
    priority=0,
    action=backup,
    argument=('/home/jileon/',),
)
t_last_backup = datetime.datetime(year, month, day, 17, 38, 20)  # (5)
scheduler.enterabs(
    t_last_backup.timestamp(),
    priority=0,
    action=backup,
    argument=('/home/jileon/',),
)

try:
    print("Esperando por eventos")
    scheduler.run(blocking=True)  # (6)
except KeyboardInterrupt:
    print('Stopped.')
