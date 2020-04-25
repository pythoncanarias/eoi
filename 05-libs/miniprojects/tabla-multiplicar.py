#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description="Tablas de multiplicar")
parser.add_argument(
    "base",
    type=int,
    help="Número de la tabla a imprimir",
    choices=list(range(1, 10)),
)
parser.add_argument(
    "-e", "--examen",
    help="No muestra los resultados",
    action='store_false',
    )

def main():
    options = parser.parse_args()
    base = options.base
    ver_resultados = options.examen
    for i in range(1, 11):
        print(f"{base} x {i:2} = ", end="")
        if ver_resultados:
            print(base * i)
        else:
            print("[    ]")

if __name__ == "__main__":
    main()
