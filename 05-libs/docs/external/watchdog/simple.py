#!/usr/bin/env python

import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

my_event_handler = FileSystemEventHandler()


def on_created(event):
    print(f"hay un nuevo {event.src_path} fichero!")


my_event_handler.on_created = on_created


def main():
    my_observer = Observer()
    my_observer.schedule(my_event_handler, '.', recursive=True)
    my_observer.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()


if __name__ == "__main__":
    main()

