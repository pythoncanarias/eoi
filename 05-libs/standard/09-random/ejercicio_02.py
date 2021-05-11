#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

from cards import Card

baraja = []
for palo in [Card.CLUB, Card.DIAMONDS, Card.SPADES, Card.HEARTS]:
    for valor in range(1, 14):
        baraja.append(Card(palo, valor))

print("Voy a repartir una mano de 5 cartas al azar")
...
