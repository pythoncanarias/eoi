import random

baraja = [
    'CA', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK',
    'RA', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'R10', 'RJ', 'RQ', 'RK',
    'TA', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'TJ', 'TQ', 'TK',
    'PA', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10', 'PJ', 'PQ', 'PK'
]

random.shuffle(baraja)
print(baraja[0:5])
