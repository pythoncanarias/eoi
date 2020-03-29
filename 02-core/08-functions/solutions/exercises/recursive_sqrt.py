EPSILON = 10e-12


def newton(x, r):
    if (r * r) - x < EPSILON:
        return r
    r = (r + x / r) / 2
    return newton(x, r)


x = 4000
print(newton(x, x / 2))
