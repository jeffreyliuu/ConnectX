# Connect X
This game is a new edition of the popular Connect 4, except users can now specify the grid size and the amount they want to connect! There is both a single-player and local two-player mode.
### Single player mode
In single player mode, the user faces a computer bot of varying selectable difficulties: `EASY, MEDIUM`, and `HARD`, with each difficulty using a different approach to select a move in the game.
- The `EASY` difficulty uses a random approach, where the bot randomnly selects a column they can put a piece into. 
- The `MEDIUM` difficulty uses a more "score-based" approach, where the bot considers every possible move it can do and assigns a score for each move:
    - The score is based on whether the placement of the piece in the move is beneficial or not. The more beneficial (ex. winning a game, blocking the opposing player from winning) a move is, the higher the score
    - At the end the bot selects the column that results in the highest achieved score.
- The `HARD` difficulty applies a more AI-based minimax algorithm that also uses alpha-beta pruning. 

### Local two-player mode
If you have friends, you can play a local two-player mode that works exactly the same way in person.

## Installation
1. Clone the repo
2. Run `python3 -m main_menu.py
3. Have fun!

## Tech stack:
- Python
- Pygame


