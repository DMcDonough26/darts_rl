
import numpy as np

class Game(object):
    def __init__(self):
        self.board = {'20':0,'19':0}
        self.darts = 0

    def get_state_and_reward(self):
        return self.board, self.give_reward()

    def give_reward(self):
        if sum(self.board.values()) == 6:
            return 0
        else:
            return -1

    def update_game(self, target, result):
        new_val = int(self.board[target])+int(result)
        if new_val > 3:
            new_val = 3
        self.board[target] = new_val
        self.darts = int(self.darts) + 1

    def is_game_over(self):
        if sum(self.board.values()) == 6:
            return True
        else:
            return False
