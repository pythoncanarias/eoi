import fire


def add(a: int, b:int) -> int:
    return a + b


def hello(name):
    """Saluda al nombre pasado como parámetro.
    """
    return f"Hello {name}!"


if __name__ == '__main__':
    fire.Fire(hello)
