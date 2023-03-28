class Player:

    def __init__(self, name):
        self.points = 0
        self.hand = []
        self.name = name
        self.bet = 0

    def add_card(self, card):
        self.hand.append(card)

    def place_a_bet(self, bet):
        self.bet = bet

    def play_card(self, card):
        self.hand.remove(card)

    def show_hand(self):
        print(self.name + "'s hand:")
        for card in self.hand:
            print(card)

    def show_bet(self):
        print(f"{self.name}'s bet: {self.bet}")
