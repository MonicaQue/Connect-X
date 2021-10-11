import os, sys
if __name__ == '__main__':
    import monitor

import random
import numpy as np

def think(observation, configuration):
    global obs, config, rows, columns, inarow, board
    global actions, alpha, gamma
    obs = observation
    config = configuration
    rows = config["rows"]
    columns = config["columns"]
    inarow = config["inarow"]
    board = np.asarray(obs["board"]).reshape(rows, columns)
    actions = range(columns)
    alpha = 0.1
    gamma = 0.75

def drop_piece(grid, column, player):
    next_grid = grid.copy()
    for row in range(rows-1, -1, -1): #5, 4, 3, 2, 1, 0
        if next_grid[row][column] == 0:
            break
    next_grid[row][column] += player
    return next_grid

# Returns true if there are already four checkers connected in the board
def connected(board, player):
    grid = np.asarray(board).reshape(rows, columns)
    # horizontal
    for row in range(rows): #fixed row
        for col in range(columns-inarow+1): #0, 1, 2, 3: left to right
            serie = list(grid[row, range(col, col+inarow)])
            if serie.count(player) == inarow: return True
    # vertical
    for row in range(rows-1, rows-inarow, -1): #5, 4, 3, bottom to top
        for col in range(columns): #fixed column
            serie = list(grid[range(row, row-inarow, -1), col])
            if serie.count(player) == inarow: return True
    # positive diagonal
    for row in range(rows-1, rows-inarow, -1): #5, 4, 3: bottom to top
        for col in range (columns-inarow+1): #0, 1, 2, 3: left to right
            serie = list(grid[range(row, row-inarow, -1), range(col, col+inarow)])
            if serie.count(player) == inarow: return True

    # negative diagonal
    for row in range(rows-inarow+1): #0, 1, 2: top to bottom
        for col in range(columns-inarow+1): #0, 1, 2, 3:left to right
            serie = list(grid[range(row, row+inarow), range(col, col+inarow)])
            if serie.count(player) == inarow: return True

def maximize(playable_actions, board):
    rewards = []
    for action in playable_actions:
        if connected(action, board, 1):
            rewards[action] = 101
        elif connected(action, board, 2):
            rewards[action] = -100
        else:
            rewards[action] = 0
    return action

def train():
    reward = 0
    for i in range(1000):
        Q = ?
        current_state = previous_action
        playable_actions = [col for col in range(columns) if board[col] == 0]
        action = maximize(playable_actions)
        #temp_diff = R[current_state, next_state] + (gamma*max_action) - Q[current_state, next_state]


def make_move():
    return 4
