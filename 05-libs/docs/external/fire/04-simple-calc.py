import fire

class Calc:

    def add(self, x, y):
        return x + y

    def multiply(self, x, y):
        return x * y

if __name__ == '__main__':
    fire.Fire(Calc)

