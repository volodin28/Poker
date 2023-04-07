from const import ROUNDS


class Player:

    def __init__(self, name):
        self.points = 0
        self.hand = []
        self.name = name
        self.bet = 0
        self.tricks = 0

    def __repr__(self):
        return self.name

    def __len__(self):
        return len(self.hand)

    def add_card(self, card):
        self.hand.append(card)

    def clear_hand(self):                                   # clear hand after round
        self.hand.clear()

    def clear_tricks(self):                                 # clear tricks after round
        self.tricks = 0

    def calculate_points(self, num_round):
        mult = 1                                            # multiplier (x2 for 'Dark' round)
        if ROUNDS[num_round] == 'Dark':
            mult = 2
        if self.tricks == self.bet == 0:
            self.points += 5 * mult
        elif self.tricks == self.bet:
            self.points += self.bet * 10 * mult
        elif self.tricks > self.bet:
            self.points += self.tricks * mult
        elif self.tricks < self.bet:
            self.points -= (self.bet - self.tricks) * 10 * mult

    def play_card(self, card_index):
        return self.hand.pop(card_index)

    def show_hand(self):
        print(f"{self.name}'s hand: {self.hand}")

    def show_bet(self):
        print(f"{self.name}'s bet: {self.bet}")

    def show_points(self):
        print(f"{self.name}'s points: {self.points}")
