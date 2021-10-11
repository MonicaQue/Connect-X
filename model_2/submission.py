def agent(observation, configuration):
    import random
    import numpy as np

    obs = observation
    board = obs["board"]
    config = configuration
    rows = config["rows"]
    columns = config["columns"]
    inarow = config["inarow"]

    def drop_piece(grid, column, player):
        next_grid = grid.copy()
        for row in range(rows-1, -1, -1): #5, 4, 3, 2, 1, 0
            if next_grid[row][column] == 0:
                break
        next_grid[row][column] += player
        return next_grid

    def winning_move(column, player, board):
        grid = np.asarray(board).reshape(rows, columns)
        next_grid = drop_piece(grid, column, player)
        # horizontal
        for row in range(rows): #fixed row
            for col in range(columns-inarow+1): #0, 1, 2, 3: left to right
                serie = list(next_grid[row, range(col, col+inarow)])
                if serie.count(player) == inarow:
                    return True
        # vertical
        for row in range(rows-1, rows-inarow, -1): #5, 4, 3, bottom to top
            for col in range(columns): #fixed column
                serie = list(next_grid[range(row, row-inarow, -1), col])
                if serie.count(player) == inarow:
                    return True
        # positive diagonal
        for row in range(rows-1, rows-inarow, -1): #5, 4, 3: bottom to top
            for col in range (columns-inarow+1): #0, 1, 2, 3: left to right
                serie = list(next_grid[range(row, row-inarow, -1), range(col, col+inarow)])
                if serie.count(player) == inarow:
                    return True

        # negative diagonal
        for row in range(rows-inarow+1): #0, 1, 2: top to bottom
            for col in range(columns-inarow+1): #0, 1, 2, 3:left to right
                serie = list(next_grid[range(row, row+inarow), range(col, col+inarow)])
                if serie.count(player) == inarow:
                    return True

    def make_move():
        valid_moves = [col for col in range(columns) if board[col] == 0]
        for move in valid_moves:
            if winning_move(move, 1, board):
                return move
        for move in valid_moves:
            if winning_move(move, 2, board):
                return move
        return random.choice(valid_moves)

    action = make_move()
    return action
