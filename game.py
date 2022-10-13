import pygame
import string

DIFFICULTY = ['EASY']
PLAYER_NAMES = ['Player 1', 'Player 2']
DIMENSIONS = [3, 3]
IS_SINGLE_PLAYER=[False]


def play_single_player(difficulty: string):
    ## WILL MAKE AI
    print(f'one player on difficulty {difficulty}')
    
    

def play_two_player(player1, player2):
    
    
    print(f'two players, player 1 is {player1}, player 2 is {player2}')



def play_game(is_single_player: bool):
    print(f'starting gmae for is single_player {is_single_player}')
    if is_single_player is True:
        play_single_player(DIFFICULTY[0])
    else:
        play_two_player(PLAYER_NAMES[0], PLAYER_NAMES[1])
    