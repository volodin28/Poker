from Deck import Deck
from const import ROUNDS
from Player import Player


class Game:

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.players = []
        self.trump_card = ""
        self.trump_suit = ""

    def make_players(self):
        num_players = input("How many players:")
        for i in range(int(num_players)):
            name = input('Enter name of player {}: '.format(i + 1))
            self.players.append(Player(name))

    def deal_cards(self, num_cards):
        for i in range(num_cards):
            for player in self.players:
                card = self.deck.deal_card()
                player.add_card(card)

    def set_trump(self):
        self.trump_card = self.deck.deal_card()
        self.trump_suit = self.trump_card.suit

    def place_a_bet(self):
        for player in self.players:
            bet = int(input(f"{player.name}, what is your bet for this round"))
            player.place_a_bet(bet)

    def play_round(self):
        num_cards = ROUNDS[0]       #####
        self.deal_cards(num_cards)
        self.set_trump()
        for player in self.players:
            player.show_hand()
        print('The trump is', self.trump_card)
        self.place_a_bet()
        for player in self.players:
            player.show_bet()
