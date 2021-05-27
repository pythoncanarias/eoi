import argparse

parser = argparse.ArgumentParser()
parser.add_argument("num", type=int, help="valor a elevar al cuadrado")
options = parser.parse_args()
print(options.num**2)

