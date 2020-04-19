import fire

def hello(name):
    """Saluda al nombre pasado como parámetro.
    """
    return f"Hello {name}!"

if __name__ == '__main__':
    fire.Fire(hello)
