"""Module responsible for creating and maintaining the Connect X board"""
import pygame
import numpy as np


class Board:
    def __init__(self, width, length) -> None:
        self.width = width
        self.length = length
        self.board = np.zeros((width, length))
    
    def print_board(self):
        
        print(np.flip(self.board, 0))

