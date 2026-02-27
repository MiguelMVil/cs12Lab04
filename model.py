# pyright: strict

from common_types import Player, WinConditionType, TokenPhysicsType


class ConnectTacToeModel:
    def __init__(self, game_mode: WinConditionType, physics: TokenPhysicsType):
        self._game_mode: WinConditionType = game_mode
        self._physics: TokenPhysicsType = physics

        self._grid: list[list[str]] = []
        # making the grid
        curr_row: list[str] = []
        for r in range(self.row_count):
            curr_row = []
            for c in range(self.col_count):
                curr_row.append('.')
            self._grid.append(curr_row)

        self._winner: Player | None = None
        self._current_player = Player

    @property
    def current_player(self) -> Player:
        pass

    @property
    def winner(self) -> Player | None:
        return self._winner

    @property
    def is_game_done(self) -> bool:
        if game_mode == WinConditionType.TIC_TAC_TOE:


        else:
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