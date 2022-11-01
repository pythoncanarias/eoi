import sys
from types import ModuleType, FunctionType
from gc import get_referents

# Custom objects know their class.
# Function objects seem to know way too much, including modules.
# Exclude modules as well.
BLACKLIST = type, ModuleType, FunctionType


def getsize(obj):
    """sum size of object & members."""
    if isinstance(obj, BLACKLIST):
        raise TypeError('getsize() does not take argument of type: '+ str(type(obj)))
    seen_ids = set()
    size = 0
    objects = [obj]
    while objects:
        need_referents = []
        for obj in objects:
            if not isinstance(obj, BLACKLIST) and id(obj) not in seen_ids:
                seen_ids.add(id(obj))
                size += sys.getsizeof(obj)
                need_referents.append(obj)
        objects = get_referents(*need_referents)
    return size

# Our code here

class IA:

    def __init__(self):
        self.space = [0] * 1000000

class Enemy:

    IA = None

    def __init__(self, name="prototype"):
        self.name = name
        if Enemy.IA is None:
            Enemy.IA = IA()

    def __repr__(self):
        return f'Enemy({repr(self.name)})'


for i in range(3):
    e = Enemy(f"enemy_{i}")
    print(e, getsize(e))

