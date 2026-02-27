# pyright: strict

from common_types import Player, WinConditionType, TokenPhysicsType


class ConnectTacToeModel:
    def __init__(self):
        # will leave this for later
        pass

    @property
    def current_player(self) -> Player:
        pass

    @property
    def winner(self) -> Player | None:
        pass

    @property
    def is_game_done(self) -> bool:
        pass

    def choose_cell(self, row: int, col: int) -> bool:
        pass

    @property
    def row_count(self) -> int:
        return 6 

    @property
    def col_count(self) -> int:
        return 7

    def get_owner(self, row: int, col: int) -> Player | None:
        pass