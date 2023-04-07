from Deck import Deck
from const import ROUNDS
from Player import Player

from random import choice


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

    def set_num_cards(self, num_round):
        if isinstance(ROUNDS[num_round], int):
            return ROUNDS[num_round]
        if isinstance(ROUNDS[num_round], str):
            return int(len(self.deck) / len(self.players))

    def set_trump(self, num_cards, dealer):
        if num_cards < len(self.deck) / len(self.players):
            self.trump_card = self.deck.deal_card()
        else:
            self.trump_card = choice(dealer.hand)
        self.trump_suit = self.trump_card.suit
        print('The trump is', self.trump_card)                          # show trump

    def set_trump_values(self, player):
        for card in player.hand:
            if card.suit == self.trump_suit:
                card.value += 10

    # 3.3 Замовлення гравців
    def place_a_bet(self, num_cards):
        sum_bets = 0
        for player in self.players:
            while True:
                try:
                    player.bet = int(input(f"{player.name}, Enter your bet 0 to {num_cards}: "))
                    # if self.players.index(player) != len(self.players) - 1:
                    if player != self.players[-1]:
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

    def play_circle(self, num_cards):
        first_player = self.players[0]  # remember the order of the table before circles within round
        table = {}
        circle_suit = ""
        for circle in range(num_cards):
            for player in self.players:
                while True:
                    try:
                        card_index = int(input(f'{player.name}, your turn: '))
                        if player == self.players[0]:
                            if 0 <= card_index <= len(player.hand):
                                circle_suit = player.hand[card_index].suit
                                table.update({player.play_card(card_index): player}) # player plays card, and it is added to 'table' dict
                                break
                            else:
                                print(f'Card index must be in the range 0 to {len(player.hand) - 1}:')
                        else:
                            player_suits = [x.suit for x in player.hand]
                            if player.hand[card_index].suit != circle_suit and circle_suit in player_suits:
                                print(f"{player.name}, you should play card with {circle_suit} suit")
                            elif circle_suit not in player_suits and player.hand[card_index].suit != self.trump_suit and self.trump_suit in player_suits:
                                print(f"{player.name}, you should play card with trump suit")
                            else:
                                if player.hand[card_index].suit != self.trump_suit and player.hand[card_index].suit != circle_suit:
                                    player.hand[card_index].value = 0
                                table.update({player.play_card(card_index): player})
                                break
                    except ValueError:
                        print(f"{player.name},Enter valid number")
            print(f"The winner is {table[max(table.keys())]}")
            self.calculate_trick(table[max(table.keys())])
            self.rotate_players_order(table[max(table.keys())])
        self.rotate_players_order(first_player)  # return players to the order before round

    def rotate_players_order_forward(self):
        self.players.append(self.players[0])
        self.players.remove(self.players[0])

    def rotate_players_order_backwards(self):
        self.players = [self.players[-1]] + self.players[:len(self.players) - 1]

    def rotate_players_order(self, first_player):
        self.players = self.players[self.players.index(first_player):] + self.players[:self.players.index(first_player)]

    def set_dealer(self, num_round):
        if num_round <= len(self.players):
            return num_round - 1
        else:
            return num_round % 4

    @staticmethod
    def calculate_trick(player):
        player.tricks += 1

    def play_round(self, num_round):
        # for num_round in ROUNDS.keys():
        self.set_dealer(num_round)                                  # set the dealer for round
        if num_round > 1:
            self.rotate_players_order(self.players[1])              # set up correct player order
        print(f"""_______________________________
ROUND {num_round}.
Dealer is {self.players[0]}
_______________________________""")
        self.deck = Deck()                                          # make a deck and shuffle cards
        num_cards = self.set_num_cards(num_round)                   # estimate number of cards to deal this round
        self.deal_cards(num_cards)                                  # deal cards to players
        self.set_trump(num_cards, self.players[0])                  # set the trump
        # self.set_trump_values()
        for player in self.players:
            self.set_trump_values(player)                           # add values to cards with trump suit
            player.show_hand()                                      # show cards of players
        self.rotate_players_order_forward()                         # rotate players order for the betting stage
        self.place_a_bet(num_cards)                                 # players make bets for the round
        self.rotate_players_order_backwards()                       # rotate players order after batting stage
        self.play_circle(num_cards)                                 # players playing cards
        for player in self.players:
            player.calculate_points()                               # calculate players points of the round
            player.show_points()                                    # show players points
            player.clear_hand()                                     # clear players hand after round
            player.clear_tricks()                                   # clear players tricks after round
