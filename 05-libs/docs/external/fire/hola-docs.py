import fire

def hola(name="Mundo"):
    """Saluda educadamente a quien se le diga.
    """
    return f"Hola, {name}!"

if __name__ == '__main__':
    fire.Fire()
