def gcd(a, b):
    '''Euclid's Algorithm'''
    while b > 0:
        a, b = b, a % b
    return a
