import time
import copy

class IA:
    def __init__(self):
        time.sleep(3)  # Simula ona operacion costosa en tiempo

class Enemy:
    def __init__(self, name="prototype"):
        print(f"Creating {name}", end="...")
        self.name = name
        self.ia = IA()
        print("[ok]")

    def __repr__(self):
        return f'Enemy({repr(self.name)})'

    def clone(self, name):
        print(f"Cloning {name} from {self.name}", end="...")
        result = copy.deepcopy(self)
        result.name = name
        print("[ok]")
        return result

enemy_prototype = Enemy()
for i in range(3):
    e = enemy_prototype.clone(f"enemy_{i}")
    print(e)


