#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import logging
import time

from watchdog.observers import Observer

from watchdog.events import PatternMatchingEventHandler


def on_created(event):
    print(f"hay un nuevo {event.src_path} fichero python!")


def monitoriza_python_files(path):
    event_handler = PatternMatchingEventHandler(patterns=["*.py"])
    event_handler.on_created = on_created
    observer = Observer()
    observer.schedule(event_handler, ".", recursive=False)
    print("Esperando creación de fichero .py")
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\nOK. Terminado")
    observer.join()


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    monitoriza_python_files(path)


if __name__ == "__main__":
    main()
