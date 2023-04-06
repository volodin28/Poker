class Player:

    def __init__(self, name):
        self.points = 0
        self.hand = []
        self.name = name
        self.bet = 0

    def __repr__(self):
        return self.name

    def __len__(self):
        return len(self.hand)

    def add_card(self, card):
        self.hand.append(card)

    def clear_hand(self):
        self.hand.clear()

    # def place_a_bet(self, bet):
    #     self.bet = bet

    def play_card(self, card_index):
        return self.hand.pop(card_index)

    def show_hand(self):
        print(f"{self.name}'s hand: {self.hand}")

    def show_bet(self):
        print(f"{self.name}'s bet: {self.bet}")
