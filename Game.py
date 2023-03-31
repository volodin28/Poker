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
        for player in self.players:
            for i in range(num_cards):
                card = self.deck.deal_card()
                player.add_card(card)

    def set_trump(self):
        self.trump_card = self.deck.deal_card()
        self.trump_suit = self.trump_card.suit

    # 3.3 Замовлення гравців
    def place_a_bet(self, num_cards):
        # num_cards = ROUNDS[1]  #####
        sum_bets = 0
        for player in self.players:
            while True:
                try:
                    player.bet = int(input(f"{player.name}, Enter your bet 0 to {num_cards}: "))
                    # player.place_a_bet(bet)
                except ValueError:
                    print(f"{player.name},Enter valid number")
                    continue
                if self.players.index(player) != len(self.players) - 1:
                    if 0 <= player.bet <= num_cards:
                        print(f"{player.name}'s bet is: {player.bet}")
                        sum_bets += player.bet
                        break
                    else:
                        print(f'The bet must be in the range 0 to {num_cards}:')
                else:
                    if 0 <= player.bet <= num_cards and player.bet != (num_cards - sum_bets):
                        print(f"{player.name}'s bet is: {player.bet}")
                        sum_bets += player.bet
                        break
                    else:
                        print(f'The bet must be in the range 0 to {num_cards} and not equal to {num_cards - sum_bets}')

    def rotate_players_order(self):
        self.players.append(self.players[0])
        self.players.remove(self.players[0])

    def play_round(self):
        for num_round in ROUNDS.keys():
            print(f"""_______________________________
ROUND {num_round}.
Dealer is {self.players[0]}
_______________________________""")
            num_cards = ROUNDS[num_round]
            print(num_cards)
            self.deal_cards(num_cards)
            self.set_trump()
            for player in self.players:
                player.show_hand()
            print('The trump is', self.trump_card)
            self.rotate_players_order()
            self.place_a_bet(num_cards)


