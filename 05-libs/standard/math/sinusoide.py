import math
import time

for x in range(2000):
    spaces = 40 + int(round(math.sin(x/180.)*40))
    print(" " * spaces, "()=()")
    time.sleep(0.01)

