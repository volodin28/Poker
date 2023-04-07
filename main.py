from Game import Game
from const import ROUNDS

if __name__ == '__main__':
    g = Game()
    g.make_players()
    for num_round in ROUNDS.keys():
        g.play_round(num_round)
