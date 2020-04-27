import sys
import socket


class CPU:

    def info(self):
        return 'Intel i8 6 cores'


class Memory:

    def info(self):
        return '64 GB'


class Hostname:
    def __init__(self):
        self.hostname = socket.gethostname()

    def info(self):
        return self.hostname


class Platform:

    def info(self):
        return sys.platform


print("Information on this computer:")
for Cls in (CPU, Memory, Hostname, Platform):
    instance = Cls()
    print(f" - {Cls.__name__}: {instance.info()}")
