#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Card:

    CLUB = 1
    DIAMONDS = 2
    SPADES = 3
    HEARTS = 4

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def get_suit_name(self):
        suit_names = {
            Card.CLUB: "Tréboles",
            Card.DIAMONDS: "Diamantes",
            Card.SPADES: "Picas",
            Card.HEARTS: "Corazones",
        }
        return suit_names[self.suit]

    def get_value_name(self):
        if self.value == 1:
            return "As"
        elif self.values == 11:
            return "Sota"
        elif self.values == 12:
            return "Reina"
        elif self.values == 13:
            return "Rey"
        else:
            return str(self.value)

    def __str__(self):
        return "{} de {}".format(
            self.get_value_name(),
            self.get_suit_name(),
            )
