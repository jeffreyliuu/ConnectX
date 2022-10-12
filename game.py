import pygame
import string


def play_single_player(difficulty: string):
    ## WILL MAKE AI
    print(f'one player on difficulty {difficulty}')

def play_two_player():
    ## will implement now
    print('two player')


def play_game(is_single_player: bool, difficulty):
    if is_single_player is True:
        play_single_player(difficulty)
    else:
        play_two_player()
        
    