"""
This is the main menu module responsible for
"""
from ast import While
from typing import Tuple, Any
import string
import pygame
import pygame_menu
from game import play_game, DIFFICULTY, PLAYER_NAMES, DIMENSIONS, IS_SINGLE_PLAYER
import numpy as np

# Constants
DEFAULT_THEME=pygame_menu.themes.THEME_BLUE


pygame.init()
pygame.display.set_caption('Connect X')
res = (720, 720)
screen = pygame.display.set_mode(res)
screen.fill((230, 230, 230))

def set_single_player_mode():
    if IS_SINGLE_PLAYER[0] is True:
        return
    print('setting single player mode')
    IS_SINGLE_PLAYER[0] = True

def set_two_player_mode():
    if IS_SINGLE_PLAYER[0] is False:
        return
    print('setting two player mode')
    IS_SINGLE_PLAYER[0] = False

def set_dimensions(dimension: int, dimension_type: string):
    """
    Verifies that the dimensions of the board are of the desired length/width
    Args:
        dimension (int): length of the dimension
        dimension (string): type of dimension
    """
    print(f'Setting dimension {dimension_type} {dimension}')
    if dimension_type == 'length':
        DIMENSIONS[1] = dimension
    if dimension_type == 'width':
        DIMENSIONS[0] = dimension


def set_player_names(player_name: string, player_num: int):
    """Method that sets the player name for a player

    Args:
        player_name (string): player name we want to set to
        player_num (int): player number (1 or 2)
    """
    print(f'Set player {player_num}\'s name to {player_name}')
    PLAYER_NAMES[player_num - 1] = player_name

def change_difficulty(value: Tuple[Any, int], difficulty: str) -> None:
    """
    Change difficulty of the game.
    :param value: Tuple containing the data of the selected object
    :param difficulty: Optional parameter passed as argument to add_selector
    """
    selected, index = value
    print(f'Selected difficulty: "{selected}" ({difficulty}) at index {index}')
    DIFFICULTY[0] = difficulty

pregame_menu = pygame_menu.Menu("Select game specification", res[0], res[1], theme=DEFAULT_THEME)
pregame_menu.add.text_input("Width of Board: ", default=3, input_type=pygame_menu.locals.INPUT_INT, onchange=set_dimensions, dimension_type='width')
pregame_menu.add.text_input("Length of Board: ", default=3, input_type=pygame_menu.locals.INPUT_INT, onchange=set_dimensions, dimension_type='length')
pregame_menu.add.button('Start', play_game, IS_SINGLE_PLAYER)


single_player_menu = pygame_menu.Menu("Single Player", res[0], res[1], theme=DEFAULT_THEME)
single_player_menu.add.selector('Select difficulty: ',
                                [('1 - EASY', 'EASY'),
                                    ('2 - MEDIUM', 'MEDIUM'),
                                    ('3 - HARD', 'HARD')], onchange=change_difficulty, selector_id='select_difficulty')
single_player_menu.add.button('Start', pregame_menu)
single_player_menu.add.button('Return to main menu', pygame_menu.events.BACK)
single_player_decorator = single_player_menu.get_decorator()
single_player_decorator.add_callable(set_single_player_mode, pass_args=False)

two_player_menu = pygame_menu.Menu("Two Players", res[0], res[1], theme=DEFAULT_THEME)
two_player_menu.add.text_input('Player 1: ', default=PLAYER_NAMES[0], onchange=set_player_names, player_num=1, maxchar=10)
two_player_menu.add.text_input('Player 2: ', default=PLAYER_NAMES[1], onchange=set_player_names, player_num=2, maxchar=10)
two_player_menu.add.button('Start', pregame_menu)
two_player_menu.add.button('Return to main menu', pygame_menu.events.BACK)
two_player_decorator = two_player_menu.get_decorator()
two_player_decorator.add_callable(set_two_player_mode, pass_args=False)


main_menu = pygame_menu.Menu("Connect X", res[0], res[1], center_content=True, theme=DEFAULT_THEME)
main_menu.add.button('Single Player', single_player_menu)
main_menu.add.button('Two Players', two_player_menu)
main_menu.add.button('Quit', pygame_menu.events.EXIT)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    if main_menu.is_enabled():
        main_menu.mainloop(screen)
    

    pygame.display.update()
