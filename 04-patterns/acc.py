import random

class _Accumulator:
    
    def __init__(self):
        print("Se llama al constructor de la clase Accumulator")
        self.value = random.randrange(1000000)
        
    def __repr__(self):
        return f"Acumulator(value={self.value})"
        
    def inc(self):
        self.value += 1


def accumulator():
    if accumulator.instance is None:
        accumulator.instance = _Accumulator()
    return accumulator.instance

accumulator.instance = None
