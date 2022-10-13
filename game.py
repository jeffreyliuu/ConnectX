# pylint: disable=[E0611, E1101]
"""Main execution of the game"""
import string
import pygame
from board import Board
import constants

pygame.init()
pygame.display.set_caption('Connect X')
screen = pygame.display.set_mode(constants.res)
screen.fill((230, 230, 230))

def play_single_player(difficulty: string):
    """Gameplay for only one player at difficulty {difficulty}"""
    ## WILL MAKE AI
    print(f'one player on difficulty {difficulty}')

def play_two_player(player1, player2):
    """Gameplay for two players"""
    print(f'two players, player 1 is {player1}, player 2 is {player2}')
    

def _play_game():
    [width, length, connect_size] = constants.DIMENSIONS
    print(f'We are connecting a length of {connect_size}')
    is_single_player = constants.IS_SINGLE_PLAYER
    board = Board(width, length)
    board.print_board()

    if is_single_player is True:
        print("Starting single player game")
        play_single_player(constants.DIFFICULTY)
    else:
        print("Starting two player game")
        play_two_player(constants.PLAYER_NAMES[0], constants.PLAYER_NAMES[1])
