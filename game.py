import pygame
import string
import pygame_menu
from board import Board

DIFFICULTY = ['EASY']
PLAYER_NAMES = ['Player 1', 'Player 2']
IS_SINGLE_PLAYER=[False]
DIMENSIONS = [7, 6, 4]


def play_single_player(difficulty: string):
    ## WILL MAKE AI
    print(f'one player on difficulty {difficulty}')

    


def play_two_player(player1, player2):
    
    
    print(f'two players, player 1 is {player1}, player 2 is {player2}')


def _play_game():
    [width, length, connect_size] = DIMENSIONS
    print(f'We are connecting a length of {connect_size}')
    is_single_player = IS_SINGLE_PLAYER[0]
    board = Board(width, length)
    board.print_board()

    if is_single_player is True:
        print("Starting single player game")
        play_single_player(DIFFICULTY[0])
    else:
        print("Starting two player game")
        play_two_player(PLAYER_NAMES[0], PLAYER_NAMES[1])
    
