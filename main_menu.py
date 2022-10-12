import string
import numpy as np
import pygame
import pygame_menu
from game import play_game
from typing import Tuple, Any
import sys
import math

# Constants
DEFAULT_THEME=pygame_menu.themes.THEME_BLUE
PLAYER_NAMES = ['Player 1', 'Player 2']
DIFFICULTY = ['EASY']

pygame.init()
res = (720, 720)
screen = pygame.display.set_mode(res)
screen.fill((230, 230, 230))

def change_difficulty(value: Tuple[Any, int], difficulty: str) -> None:
    """
    Change difficulty of the game.
    :param value: Tuple containing the data of the selected object
    :param difficulty: Optional parameter passed as argument to add_selector
    """
    selected, index = value
    print(f'Selected difficulty: "{selected}" ({difficulty}) at index {index}')
    DIFFICULTY[0] = difficulty

def set_name(name1, name2):
    print(f'Player 1 is {name1} and Player 2 is {name2}')
    PLAYER_NAMES[0] = name1
    PLAYER_NAMES[1] = name2
    
def main_background():
    screen.fill((230, 10, 230))
    

single_player_menu = pygame_menu.Menu("Single Player", res[0], res[1], theme=DEFAULT_THEME)
single_player_menu.add.selector('Select difficulty', 
                                [('EASY', 'EASY'),
                                    ('MEDIUM', 'MEDIUM'),
                                    ('HARD', 'HARD')], onchange=change_difficulty, selector_id='select_difficulty')
single_player_menu.add.button('Start', play_game, True, DIFFICULTY[0])
single_player_menu.add.button('Return to main menu', pygame_menu.events.BACK)

two_player_menu = pygame_menu.Menu("Two Players", res[0], res[1], theme=DEFAULT_THEME)
two_player_menu.add.text_input('Player 1: ', default=PLAYER_NAMES[0])
two_player_menu.add.text_input('Player 2: ', default=PLAYER_NAMES[1])
two_player_menu.add.button('Start', play_game, False, DIFFICULTY[0])
two_player_menu.add.button('Return to main menu', pygame_menu.events.BACK)


main_menu = pygame_menu.Menu("Connect X", res[0], res[1], center_content=True, theme=DEFAULT_THEME)
main_menu.add.button('Single Player', single_player_menu)
main_menu.add.button('Two Players', two_player_menu)
main_menu.add.button('Quit', pygame_menu.events.EXIT)   

main_background()

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
    
    if main_menu.is_enabled():
        main_menu.mainloop(screen, main_background)
    
    pygame.display.update()


