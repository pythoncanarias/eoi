# threads.py

import logging
import random
import threading
import time
from collections import deque

logging.basicConfig(level=logging.INFO, format="%(message)s")


def wait_between(mins, maxs):
    time.sleep(random.randrange(mins, maxs+1))


def produce(queue, size):
    while True:
        if len(queue) < size:
            value = random.randrange(10)
            queue.append(value)
            logging.info("Produced: %d -> %r", value, queue)
        else:
            logging.info("Queue is saturated")
        wait_between(1, 5)


def consume(queue):
    while True:
        try:
            value = queue.popleft()
        except IndexError:
            logging.info("Queue is empty")
        else:
            logging.info("Consumed: %d -> %r", value, queue)
        wait_between(2, 7)


logging.info("Starting Threads...\n")
logging.info("Press Ctrl+C to interrupt the execution\n")

shared_queue = deque()
threading.Thread(target=produce, args=(shared_queue, 10)).start()
threading.Thread(target=consume, args=(shared_queue,)).start()
