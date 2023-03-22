from random import shuffle

from const import SUITS, RANKS, POINTS


class Card:

    def __init__(self, suit, rank, points):
        self.suit = suit
        self.rank = rank
        self.points = points

    def __str__(self):
        message = f'{self.rank} {self.suit}\nPoints: {self.points}'
        return message


class Deck:

    def __init__(self):
        self.deck = self.create_deck()
        shuffle(self.deck)

    def create_deck(self):
        deck = []
        for suit in SUITS:
            for rank in RANKS:
                points = POINTS.get(rank)
                c = Card(suit=suit, rank=rank, points=points)
                deck.append(c)
        return deck

