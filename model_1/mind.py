import os, sys
if __name__ == '__main__':
    import monitor

import random

def think(observation, configuration):
    global obs, config, rows, columns, board
    obs = observation
    config = configuration
    board = obs["board"]
    rows = config["rows"]
    columns = config["columns"]

def validate(move):
    for i in range(columns):
        if obs.board[move] == 0:
            return True
        else:
            return False


def make_move():
    move= 4
    while validate(move):
        move = random.randint(0, 6)
        return move
