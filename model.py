# pyright: strict

from common_types import Player, WinConditionType, TokenPhysicsType

class ConnectTacToeModel:
    ROWS, COLUMNS = 6, 7

    def __init__(self, win_condition_type, token_physics_type):
        self._grid = [[None for _ in range(self.COLUMNS)] for _ in range(self.ROWS)]
        self._current_player = Player.P1
        self._winner = None
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

    @property
    def grid(self):
        return self._grid
        
    def choose_cell(self, row: int, col: int) -> bool:
        if self._is_game_done:
            return False
        if (0 <= row <= SELF.ROWS) or (0 <= col <= SELF.COLUMNS) 
            return False
        if self._grid[row][col] is not None:
            return False

        self._grid[row][col] = self._current_player
        self.winner_checker(self._current_player)

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

    def winner_checker(self, player):
        for row in range(self.ROWS):
            checker = line_checker([(row, col) for col in range(self.COLUMNS)])
            if checker:
                self._winner = player
                self._is_game_done = True

        for row in range(self.COLUMNS):
            checker = line_checker([(row, col) for row in range(self.ROWS)])
            if checker:
                self._winner = player
                self._is_game_done = True

        return None

    def line_checker(self, line):
        for x in range(1, len(line) - 1):
            row, col = line[x]
            past_row, past_col = line[x - 1]
            next_row, next_col = line[x + 1]
            current_cell = self._grid[row][col]
            past_cell = self._grid[past_row][past_col]
            next_cell = self._grid[next_row][next_col]
            if (current_cell == past_cell == next_cell) and current_cell is not None:
                return True
            return False
        
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
