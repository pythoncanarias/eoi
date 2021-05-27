import random

from cards import Card

baraja = []
for palo in [Card.CLUB, Card.DIAMONDS, Card.SPADES, Card.HEARTS]:
    for valor in range(1, 14):
        baraja.append(Card(palo, valor))

print("Voy a elegir una carta al azar")
card = ...
print(card)
