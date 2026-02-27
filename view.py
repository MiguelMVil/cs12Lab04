# pyright: strict

from common_types import Player
from collections.abc import Sequence

class ConnectTacToeView:
    def __init__(self):
        pass

    def print_grid(self, grid: list[list[Player | None]]) -> None:

        grid_header: str = 'X 1 2 3 4 5 6 7' 

        print(grid_header)

        for row in range(1, 7):
            curr_row: str = str(row) + ' '

            for cell in grid[row - 1]:
                if cell is Player.P1:
                    curr_row += 'X'
                elif cell is Player.P2:
                    curr_row += 'O'
                else:
                    curr_row += '.'

            print(curr_row)

    def print_player(self, player: Player):
        if player is Player.P1:
            print("Currently Playing: Player 1")
        else:
            print("Currently Playing: Player 2")

    def print_winner(self, player: Player | None):
        if player is Player.P1:
            print("Player 1 has won the game!")
        elif player is Player.P2:
            print("Player 2 has won the game!")
        else:
            print("Both players win!")

    def print_draw(self):
        print('Sadly, the game is a draw...')

    def get_input(self, failed_in_past: bool = False) -> Sequence[int]:
        i, j = -1, -1

        if failed_in_past:
            print('That was an invalid square, choose again!')

        while not 1 <= i < 7:
            try:
                i = int(input('Choose a row [1 - 7]: '))
            except KeyboardInterrupt:
                exit()
            except:
                pass

        while not 1 <= i < 6:
            try:
                j = int(input('Choose a column [1 - 6]: '))
            except KeyboardInterrupt:
                exit()
            except:
                pass

        return (i, j)
            
        


