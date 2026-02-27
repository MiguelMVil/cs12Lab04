# pyright: strict

from common_types import Player, WinConditionType, TokenPhysicsType

class ConnectTacToeModel:
    def __init__(self, win_con: WinConditionType, token_p6: TokenPhysicsType):
        self._win_con: WinConditionType = win_con
        self._token_p6: TokenPhysicsType = token_p6

        self._current_player: Player = Player.P1
        self._winner: Player | None = None
        self._is_game_done: bool = False
        self._grid: list[list[Player | None]] = [[None for _ in range(self.col_count)] 
                                                 for _ in range(self.row_count)]

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
    def row_count(self) -> int:
        return 6

    @property
    def col_count(self) -> int:
        return 7

    @property
    def grid(self) -> list[list[Player | None]]:
        return self._grid
        
    def choose_cell(self, row: int, col: int) -> bool:
        if self._is_game_done or self.get_owner(row, col) is not None:
            return False

        self._grid[row][col] = self._current_player
        self.winner_checker(self._current_player)

        if self.grid_checker() and not self._is_game_done:
            self._is_game_done = True
            return False

        if self._is_game_done:
            return False

        if not self._is_game_done:
            self.elapse_player_turn

        return True

    def get_owner(self, row: int, col: int) -> Player | None:
        return self._grid[row][col] if self._grid[row][col] is not None else None

    def winner_checker(self, player: Player):
        if self._win_con is WinConditionType.TIC_TAC_TOE:
            pass
            # tic tac toe code here

            # for row in range(self.row_count):
            #     checker: bool = line_checker([(row, col) for col in range(self.COLUMNS)])
            #     if checker:
            #         self._winner = player
            #         self._is_game_done = True

            # for row in range(self.COLUMNS):
            #     checker = line_checker([(row, col) for row in range(self.ROWS)])
            #     if checker:
            #         self._winner = player
            #         self._is_game_done = True
        else:
            pass


    # def line_checker(self, line: list[tuple[int, int]]) -> bool:
    #     for x in range(1, len(line) - 1):
    #         row, col = line[x]
    #         past_row, past_col = line[x - 1]
    #         next_row, next_col = line[x + 1]
    #         current_cell = self._grid[row][col]
    #         past_cell = self._grid[past_row][past_col]
    #         next_cell = self._grid[next_row][next_col]
    #         if (current_cell == past_cell == next_cell) and current_cell is not None:
    #             return True
    #     return False
        
    def grid_checker(self):
        return all(self._grid[row][col] is not None
            for row in range(self.row_count) 
            for col in range(self.col_count)
            )

    def elapse_player_turn(self):
        if self.current_player == Player.P1:
            self._current_player = Player.P2
        else:
            self._current_player = Player.P1
