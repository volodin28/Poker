from random import shuffle

from const import SUITS, RANKS, VALUE


class Card:

    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        message = f'{self.rank} of {self.suit}'  # Value: {self.value}
        return message

    def __repr__(self):
        return f'{self.rank} of {self.suit}'  # Value: {self.value}

    def __lt__(self, other):
        return self.value < other.value


class Deck:

    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                value = VALUE.get(rank)
                self.cards.append(Card(suit=suit, rank=rank, value=value))
        shuffle(self.cards)

    def __len__(self):
        return len(self.cards)

    def __repr__(self):
        return self.cards

    # def shuffle(self):
    #     shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop(0)
