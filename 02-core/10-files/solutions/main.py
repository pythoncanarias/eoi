import sys

import xmath

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: main.py x1 x2 x3...')
    else:
        data = [int(v) for v in sys.argv[1:]]
        print(f'Sum: {xmath.xsum(data)}')
        print(f'Max: {xmath.xmax(data)}')
        print(f'Min: {xmath.xmin(data)}')
        print(f'Avg: {xmath.xavg(data):.2f}')
        print(f'Std: {xmath.xstd(data):.2f}')
