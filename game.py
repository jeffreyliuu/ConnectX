# pylint: disable=[E0611, E1101]
"""Main execution of the game"""
import string
import math
import sys
import pygame
from board import Board
import constants

pygame.init()

SQUARESIZE = constants.SQUARE_SIZE
width = constants.DIMENSIONS[0] * SQUARESIZE
height = (constants.DIMENSIONS[1] + 1) * SQUARESIZE
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
screen.fill((228,230,246,255))
RADIUS = constants.RADIUS
myfont = pygame.font.SysFont("monospace", 75)


def draw_board(board: Board):
    """Method to update the screen with the new board

    Args:
        board (Board): board we are updating
    """
    grid = board.board
    board_height = (board.length + 1) * SQUARESIZE

    for column in range(board.width):
        for row in range(board.length):
            pygame.draw.rect(screen,
                             constants.BLUE,
                             (column*SQUARESIZE,row*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen,
                               constants.WHITE,
                               (int(column*SQUARESIZE+SQUARESIZE/2),
                                int(row*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)),
                               RADIUS)

    for column in range(board.width):
        for row in range(board.length):
            if grid[row][column] == 1:
                pygame.draw.circle(screen,
                                   constants.RED,
                                   (int(column*SQUARESIZE+SQUARESIZE/2),
                                    board_height-int(row*SQUARESIZE+SQUARESIZE/2)),
                                   RADIUS)
            elif grid[row][column] == 2:
                pygame.draw.circle(screen,
                                   constants.YELLOW,
                                   (int(column*SQUARESIZE+SQUARESIZE/2),
                                    board_height-int(row*SQUARESIZE+SQUARESIZE/2)),
                                   RADIUS)

    pygame.display.update()

def play_single_player(difficulty: string):
    """Gameplay for only one player at difficulty {difficulty}"""
    ## WILL MAKE AI
    print(f'one player on difficulty {difficulty}')

def play_two_player(board: Board, player1: string, player2: string):
    """Gameplay for two players"""
    print(f'two players, player 1 is {player1}, player 2 is {player2}')

    game_over = False
    turn = 0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, constants.WHITE, (0,0, width, SQUARESIZE))
                posx = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(screen, constants.RED, (posx, int(SQUARESIZE/2)), RADIUS)
                else:
                    pygame.draw.circle(screen, constants.YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, constants.WHITE, (0, 0, width, SQUARESIZE))
                # Ask for Player 1 Input
                if turn == 0:
                    posx = event.pos[0]
                    col = int(math.floor(posx/SQUARESIZE))

                    if board.is_valid_location(col):
                        row = board.get_next_open_row(col)
                        board.drop_piece(row, col, 1)
                        turn += 1
                        turn = turn % 2
                        if board.is_winning_move(1):
                            print('gg red')
                            label = myfont.render("Player 1 wins!!", 1, constants.RED)
                            screen.blit(label, (20, 10))
                            game_over = True

                # # Ask for Player 2 Input
                else:
                    posx = event.pos[0]
                    col = int(math.floor(posx/SQUARESIZE))

                    if board.is_valid_location(col):
                        row = board.get_next_open_row(col)
                        board.drop_piece(row, col, 2)
                        turn += 1
                        turn = turn % 2
                        if board.is_winning_move(2):
                            print('gg yellow')
                            label = myfont.render("Player 2 wins!!", 1, constants.YELLOW)
                            screen.blit(label, (20, 10))
                            game_over = True

                board.print_board()
                draw_board(board)

                if game_over:
                    pygame.time.wait(3000)

def _play_game():
    [col_num, row_num, connect_size] = constants.DIMENSIONS
    print(f'We are connecting a length of {connect_size} in dimensions {col_num} x {row_num}')
    is_single_player = constants.IS_SINGLE_PLAYER

    board = Board(col_num, row_num, connect_size)
    board.print_board()
    draw_board(board)
    pygame.display.update()

    if is_single_player is True:
        print("Starting single player game")
        play_single_player(constants.DIFFICULTY)
    else:
        print("Starting two player game")
        play_two_player(board, constants.PLAYER_NAMES[0], constants.PLAYER_NAMES[1])

    exit()
