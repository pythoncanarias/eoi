import random

with open('temperatures.txt', 'w') as f:
    for month in range(12):
        buf = []
        for day in range(31):
            buf.append(str(random.randint(10, 40)))
        f.write(','.join(buf) + '\n')
