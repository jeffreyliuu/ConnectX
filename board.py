"""Module responsible for creating and maintaining the Connect X board"""
import math
import copy
import random
import numpy as np
import constants

class Board:
    """Board class responsible for printing and maintaining the game board
    """
    def __init__(self, width, length, connect_size) -> None:
        self.width = width
        self.length = length
        self.connect_size = connect_size
        self.board = np.zeros((length, width))

    def print_board(self):
        """Method responsible for printing the board into the console
        """
        print(np.flip(self.board, 0))

    def drop_piece(self, row: int, col: int, piece: int) -> None:
        """Method that inserts a piece into coordinate (row, col)

        Args:
            row (int): row number
            col (int): column number
            piece (int): 1 or 2, depending on player number
                            1 = RED, 2 = YELLOW
        """
        self.board[row][col] = piece

    def is_valid_location(self, col):
        """Method that determines if putting a piece in column col is valid

        Args:
            col (int): column number
        """
        return self.board[self.length - 1][col] == 0

    def get_next_open_row(self, col):
        """Method that finds the next open row in column col

        Args:
            col (int): column number
        """
        for row in range(self.length):
            if self.board[row][col] == 0:
                return row
        return -1

    def is_winning_move(self, piece):
        """Determines if the piece placed is a winning move or not

        Args:
            piece (int): 1 or 2, where 1 = Player 1 and 2 = Player 2
        """

        column_count = self.width
        row_count = self.length

        ## Vertical check
        for column in range(column_count):
            for row in range(row_count - (self.connect_size - 1)):
                if self.board[row][column] == piece:
                    for i in range(1, self.connect_size):
                        if self.board[row + i][column] != piece:
                            break
                        if i is self.connect_size - 1:
                            return True

        ## Horizontal check
        for column in range(column_count - (self.connect_size - 1)):
            for row in range(row_count):
                if self.board[row][column] == piece:
                    for i in range(1, self.connect_size):
                        if self.board[row][column + i] != piece:
                            break
                        if i is self.connect_size - 1:
                            return True

        # Positive slope check
        for column in range(column_count - (self.connect_size - 1)):
            for row in range(row_count - (self.connect_size - 1)):
                if self.board[row][column] == piece:
                    for i in range(1, self.connect_size):
                        for i in range(1, self.connect_size):
                            if self.board[row + i][column + i] != piece:
                                break
                            if i is self.connect_size - 1:
                                return True

        # Negative slope check
        for column in range(column_count - (self.connect_size - 1)):
            for row in range(self.connect_size - 1, row_count):
                if self.board[row][column] == piece:
                    for i in range(1, self.connect_size):
                        for i in range(1, self.connect_size):
                            if self.board[row - i][column + i] != piece:
                                break
                            if i is self.connect_size - 1:
                                return True

    def is_full(self):
        """Determines if the board is full of pieces"""
        return len(self.get_valid_locations()) == 0

    def get_valid_locations(self):
        """Returns a list of all valid columns in the board
        """
        valid_locations = []
        for column in range(self.width):
            if self.is_valid_location(column):
                valid_locations.append(column)
        return valid_locations

    def score_position(self):
        """Determines the score if an AI drops a piece in a column given
        the current state of the board

        Returns:
            int: score of the given column position
        """
        score = 0

        # Pieces in center column have higher score
        center_array = [int(i) for i in list(self.board[:, self.width //2])]
        center_count = center_array.count(2)
        score += center_count * 3

        # Calculate score for horizontal
        for row in range(self.length):
            row_array = [int(i) for i in list(self.board[row, :])]
            for column in range(self.width - (self.connect_size - 1)):
                window = row_array[column:column + self.connect_size]
                score += self.window_value(window)

        # Calculate score for vertical
        for column in range(self.width):
            col_array = [int(i) for i in list(self.board[:,column])]
            for row in range(self.length - (self.connect_size - 1)):
                window = col_array[row: row + self.connect_size]
                score += self.window_value(window)

        # Positive value slopes
        for row in range(self.length - (self.connect_size - 1)):
            for column in range(self.width - (self.connect_size - 1)):
                window = [self.board[row + i][column + i] for i in range(self.connect_size)]
                score += self.window_value(window)

        # Negative value slopes
        for row in range(self.length - (self.connect_size - 1)):
            for column in range(self.width - (self.connect_size - 1)):
                window = [self.board[row + (self.connect_size - 1) - i][column + i] for i in
                          range(self.connect_size)]
                score += self.window_value(window)

        return score

    def window_value(self, window):
        """Determines the score for a given window of the board

        Args:
            window (list(int)): array of pieces (also empty)

        Returns:
            int: score of given window
        """
        score = 0
        num_pieces = window.count(2)
        empty_pieces = window.count(0)

        for test_size in range(self.connect_size):
            if num_pieces == self.connect_size:
                score += 100
            if num_pieces == 0 and empty_pieces == 1:
                score -= 1000
            if num_pieces == (self.connect_size - test_size) and empty_pieces == test_size:
                score += test_size + 10
        return score

    def is_terminal_node(self):
        """Determines if the game is at a halting state

        Returns:
            bool: true if the game is at a halting state, false otherwise
        """
        return self.is_winning_move(constants.PLAYER_PIECE) or self.is_winning_move(constants.AI_PIECE) or self.is_full()

    def minimax(self, depth, alpha, beta, maximizing_player: bool):
        """Recursive algorithm that determines optimal move using minimax and alpha-beta pruning

        Args:
            depth (int): recursion depth
            alpha (int): _description_
            beta (int): _description_
            maximizingPlayer (bool): determines if we are maximizing player or not

        Returns:
            int, int: first val is column index, second value is score at recursion depth
        """
        valid_locations = self.get_valid_locations()
        is_terminal = self.is_terminal_node()
        if depth == 0 or is_terminal:
            if is_terminal:
                if self.is_winning_move(constants.AI_PIECE):
                    return (None, 1000000000000)
                elif self.is_winning_move(constants.PLAYER_PIECE):
                    return (None, -1000000000000)
                else:
                    return (None, 0)
            else:
                return (None, self.score_position())
        if maximizing_player:
            min_value = -math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = self.get_next_open_row(col)
                temp_copy = copy.deepcopy(self)
                temp_copy.drop_piece(row, col, constants.AI_PIECE)
                new_score = temp_copy.minimax(depth - 1, alpha, beta, False)[1]
                if new_score > min_value:
                    min_value = new_score
                    column = col
                alpha = max(alpha, min_value)
                if alpha >= beta:
                    break
            return column, min_value
        else:
            max_value = math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = self.get_next_open_row(col)
                temp_copy = copy.deepcopy(self)
                temp_copy.drop_piece(row, col, constants.PLAYER_PIECE)
                new_score = temp_copy.minimax(depth - 1, alpha, beta, True)[1]
                if new_score < max_value:
                    max_value = new_score
                    column = col
                beta = min(beta, max_value)
                if alpha >= beta:
                    break
            return column, max_value
