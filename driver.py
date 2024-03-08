
# https://towardsdatascience.com/hands-on-introduction-to-reinforcement-learning-in-python-da07f7aaca88

import numpy as np
import pandas as pd
from game import Game
from player import Player

# create game and player

game = Game()
# player = Player(game.board)
player = Player()
dart_count = []

# create lists for dataframe
game_num_list = []
turn_num_list = []
state_list = []
target_list = []
result_list = []

# create loop for games
for i in range(5):

    j = 0

    while not game.is_game_over():

        # get the state
        state, _ = game.get_state_and_reward()

        # choose and action
        target = player.choose_target()
        result = player.get_outcome(target)

        # append to lists
        game_num_list.append(i+1)
        turn_num_list.append(j+1)
        state_list.append(dict(state))
        target_list.append(str(target))
        result_list.append(int(result))

        # update the game
        game.update_game(target[1:], result)

        # get the new state and the reward
        state, reward = game.get_state_and_reward()

        # update the state history
        player.update_state_history(state, reward)

        j += 1

    # have the agent learn
    pass

    # add the game history
    dart_count.append(game.darts)

    # create a new game
    game = Game()

# plot number of steps
print(dart_count)

result_df = pd.DataFrame({'Game':game_num_list,'Turn':turn_num_list,'State':state_list,'Target':target_list,'Result':result_list})
print(result_df[result_df['Game']==np.argmin(dart_count)+1])
