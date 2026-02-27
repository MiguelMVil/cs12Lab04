# pyright: strict

from common_types import Player, WinConditionType, TokenPhysicsType


class ConnectTacToeModel:
    ROWS, COLUMNS = 6, 7
    
    def __init__(self, game_mode: WinConditionType, physics: TokenPhysicsType):
        self._game_mode: WinConditionType = game_mode
        self._physics: TokenPhysicsType = physics

        self._grid = [[None for _ in range(self.COLUMNS)] for _ in range(self.ROWS)]
        self._winner: Player | None = None
        self._current_player = Player
        self._is_game_done = False

    @property
    def current_player(self) -> Player:
        return self._current_player

    @property
    def winner(self) -> Player | None:
        return self._winner

    @property
    def is_game_done(self) -> bool:
        return self._is_game_done
    
    @property
    def row_count(self):
        return self.ROWS

    @property
    def col_count(self):
        return self.COLUMNS

    def choose_cell(self, row: int, col: int) -> bool:
        if self._is_game_done:
            return False
        if (0 <= row <= SELF.ROWS) or (0 <= col <= SELF.COLUMNS) 
            return False
        if self._grid[row][col] is not None:
            return False

        self._grid[row][col] = self._current_player
        self.winner_checker()

        if grid_checker and not self._is_game_done:
            self._is_game_done = True
            return False

        if self._is_game_done:
            return False

        if not self._is_game_done:
            self.player_turn

        return True
        
    def get_owner(self, row: int, col: int) -> Player | None:
        return self._grid[row][col] if self._grid[row][col] is not None else None

    def winner_checker(self):
        pass   
        
    def grid_checker(self):
        return all(self._grid[row][col] is not None
            for row in range(self.ROWS) 
            for col in range(self.COLUMNS)
            )

    def player_turn(self, player):
        if self.current_player == Player.P1:
            self._current_player = Player.P2
        else:
            self._current_player = Player.P1
