import matplotlib.pyplot as plt
import random

def dice(faces=6):
    return random.randrange(1, faces + 1)

data = [dice()+dice() for _ in range(10000)]
plt.hist(data, bins = 11, color='brown', alpha=0.8)
plt.show()
