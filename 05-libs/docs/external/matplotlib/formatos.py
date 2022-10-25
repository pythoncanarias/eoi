import random
import matplotlib.pyplot as plt

markers = [
    ".", ",", "o", "v", "^", "<",
    ">", "1", "2", "3", "4", "s",
    "p", "*", "h", "H", "+", "x",
    "D", "d", "|", "_",
    ]
lines = ["-", "--", "-.", ":"]
colors = ["b", "g", "r", "c", "m", "y", "k", "w"]

line_format = random.choice(colors) + random.choice(markers) + random.choice(lines)

plt.plot([0, 1, 4, 9, 16, 25, 36], line_format)
plt.title(f"Formato: {line_format}")
plt.show()
