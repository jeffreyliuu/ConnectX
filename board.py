"""Module responsible for creating and maintaining the Connect X board"""
import numpy as np

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

    def drop_piece(self, row: int, col: int, piece: int):
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
                    print(f'{row}, {column}')
                    for i in range(1, self.connect_size):
                        if self.board[row + i][column] != piece:
                            break
                        if i is self.connect_size - 1:
                            return True

        ## Horizontal check
        for column in range(column_count - (self.connect_size - 1)):
            for row in range(row_count):
                if self.board[row][column] == piece:
                    print(f'{row}, {column}')
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
