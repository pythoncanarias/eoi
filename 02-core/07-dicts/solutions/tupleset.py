data = ((4, 3), (3, 2), (7, 4), (8, 2), (9, 1))

A, B = set(), set()
for duple in data:
    A.add(duple[0])
    B.add(duple[1])

I = A & B
print(I)
