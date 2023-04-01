from Deck import Deck
from const import ROUNDS
from Player import Player


class Game:

    def __init__(self):
        self.deck = Deck()
        # self.deck.shuffle()
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
        sum_bets = 0
        for player in self.players:
            while True:
                try:
                    player.bet = int(input(f"{player.name}, Enter your bet 0 to {num_cards}: "))
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
                            print(
                                f'The bet must be in the range 0 to {num_cards} and not equal to {num_cards - sum_bets}')
                except ValueError:
                    print(f"{player.name},Enter valid number")
                    continue

    def play_circle(self):
        table = []
        for player in self.players:
            while True:
                try:
                    card_i = int(input(f'{player.name}, your turn: '))
                    if 0 <= card_i <= len(player.hand):
                        player.play_card(player.hand[card_i])  # card to put on the table
                        break
                    else:
                        print(f'Card index must be in the range 0 to {len(player.hand) - 1}:')
                except ValueError:
                    print(f"{player.name},Enter valid number")

            print(player.hand)
            print(table)
            # player.play_card(player.hand[card_i])

    def rotate_players_order(self):
        self.players.append(self.players[0])
        self.players.remove(self.players[0])

    def play_round(self):
        for num_round in ROUNDS.keys():
            print(f"""_______________________________
ROUND {num_round}.
Dealer is {self.players[0]}
_______________________________""")
            self.deck = Deck()  # make a deck and shuffle cards
            # print(len(self.deck)) check number of cards before dealing
            num_cards = ROUNDS[num_round]  # estimate number of cards to deal this round
            self.deal_cards(num_cards)  # deal cards to players
            for player in self.players:   # show cards of players
                player.show_hand()
            self.set_trump()    # set the trump
            print('The trump is', self.trump_card)  # show trump
            # print(len(self.deck)) # check number of cards after dealing
            self.rotate_players_order()     # rotate players order
            self.place_a_bet(num_cards)   # players make bets for the round
            self.play_circle()  # players playing cards
            # for player in self.players:
            #     player.clear_hand()
