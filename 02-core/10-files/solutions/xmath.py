import math


def xsum(data):
    return sum(data)


def xmax(data):
    return max(data)


def xmin(data):
    return min(data)


def xavg(data):
    return xsum(data) / len(data)


def xstd(data):
    avg = xavg(data)
    f1 = sum(((x - avg) ** 2 for x in data))
    N = len(data) - 1
    std = math.sqrt(f1 / N)
    return std
