#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import logging
import time

from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

def monitoriza(path):
    logging.basicConfig(
        level=logging.INFO,
        format='%(name)s %(asctime)s - %(message)s',
        datefmt='%Y-%m-%dT%H:%M:%S',
    )
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, ".", recursive=False)
    print("Esperando eventos...")
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("Terminado")
    observer.join()


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    monitoriza(path)


if __name__ == "__main__":
    main()
