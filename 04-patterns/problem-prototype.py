import time


class IA:
    def __init__(self):  # Simula una operación costosa en tiempo
        time.sleep(1)
        print(".", end="", flush=True)
        time.sleep(1)
        print(".", end="", flush=True)
        time.sleep(1)
        print(".", end="", flush=True)


class Enemy:
    def __init__(self, name="prototype"):
        print(f"Creating {name}", end=":", flush=True)
        self.name = name
        self.ia = IA()
        print("[ok]", flush=True)

    def __repr__(self):
        return f'Enemy({repr(self.name)})'


def main():
    for i in range(3):
        Enemy(f"enemy_{i}")


if __name__ == "__main__":
    main()
