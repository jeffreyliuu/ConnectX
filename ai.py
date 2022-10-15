"""Module responsible for ai moves"""
import copy
import string
import random
from board import Board
import constants

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

def medium_ai_move(board: Board):
    """Returns a score-based "best" column as "MEDIUM" difficulty

    Args:
        board (Board): current board in the game

    Returns:
        int: column index
    """
    valid_locations = board.get_valid_locations()
    best_score = -10000
    best_col = random.choice(valid_locations)
    for col in valid_locations:
        row = board.get_next_open_row(col)
        temp_board = copy.deepcopy(board)
        temp_board.drop_piece(row, col, 2)
        score = temp_board.score_position()
        if score > best_score:
            best_score = score
            best_col = col

    return best_col

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
    if difficulty == 'MEDIUM':
        return medium_ai_move(board)
