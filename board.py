"""Module responsible for creating and maintaining the Connect X board"""
import pygame
import numpy as np


class Board:
    """Board class responsible for printing and maintaining the game board
    """
    def __init__(self, width, length) -> None:
        self.width = width
        self.length = length
        self.board = np.zeros((length, width))

    def print_board(self):
        """Method responsible for printing the board into the console
        """
        print(np.flip(self.board, 0))
