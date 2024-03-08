
import numpy as np

# class Player(object):
#     def __init__(self, states, alpha=0.15, random_factor=0.2):
#         self.state_history = []
#         self.alpha = alpha
#         self.random_factor = random_factor
#
#         # start the rewards table
#         self.G = {}
#         self.init_reward(states)

class Player(object):
    def __init__(self):
        self.state_history = []

    def choose_target(self):
        next_dart = None
        next_dart = np.random.choice(['T20','T19','S20','S19'])
        return next_dart

    def get_outcome(self, target):
        value = np.random.rand()
        if target[:1] == 'T':
            if value <= 0.1:
                return 3
            elif value <= 0.5:
                return 1
            else:
                return 0

        elif target[:1] == 'S':
            if value <= 0.6:
                return 1
            elif value <= 0.65:
                return 3
            else:
                return 0
        else:
            return 0

    def update_state_history(self, state, reward):
        self.state_history.append((dict(state), int(reward)))

    # def init_reward(self, states):
    #     for i, row in enumerate(states):
    #         for j, col in enumerate(row):
    #             self.G[(j,i)] = np.random.uniform(high=1.0, low=0.1)
