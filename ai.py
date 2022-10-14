"""Module responsible for ai moves"""

import string
from board import Board
import constants
import random

def easy_ai_move(board: Board):
    """Return a randomly generated column as "EASY" difficulty.

    Args:
        board (Board): current board in the game

    Returns:
        int: column index
    """
    col = random.randint(0, board.width - 1)
    while not board.is_valid_location(col):
        col = random.randint(0, board.width - 1)
    return col

def ai_choose_move(board: Board, difficulty: string):
    """Returns a specific column number determined by both the state 
    of the board and the difficulty of the AI the person is facing

    Args:
        board (Board): current board in the game
        difficulty (string): which difficulty AI we ware facing (EASY, MEDIUM, HARD)

    Returns:
        (int): column index
    """
    if difficulty == 'EASY':
        return easy_ai_move(board)
    