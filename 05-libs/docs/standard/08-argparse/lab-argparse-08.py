import argparse

parser = argparse.ArgumentParser()
parser.add_argument("num", type=int, help="valor a elevar al cuadrado")
parser.add_argument(
        "--explicacion",
        help="Muestra los pasos previos",
        action='store_true',
        )

options = parser.parse_args()
if options.explicacion:
    print(f"{options.num}^2 = {options.num**2}")
else:
    print(options.num**2)
