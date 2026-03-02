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
    
    def place_token(self, row: int, col: int):
        # Place token in the given row, col
        self._grid[row][col] = self.current_player

    def elapse_player_turn(self):
        # Elapse the turn of player
        if self.current_player == Player.P1:
            self._current_player = Player.P2
        else:
            self._current_player = Player.P1

    def choose_cell(self, row: int, col: int) -> bool:
        # Check if the cell is occupied or not
        if self._grid[row][col] is not None:
            return False
        else:
            self.place_token(row, col)
            return True
    
    def check_len_cells(self, cells: set[Player | None]):
        # Get the length of the set of row/col
        if len(cells) == 1 and None not in cells:
            self._is_game_done = True
            self._winner = self._current_player
    
    def check_rows(self):
        # Check the rows in the grid
        for row in range(self.row_count):
            cells: set[Player | None] = set()
            for col in range(self.col_count):
                cells.add(self.grid[row][col])
            # print(cells)  # check the cells being added
            self.check_len_cells(cells)

    def check_cols(self):
        # Check the cols in the grid
        for col in range(self.row_count):
            cells: set[Player | None] = set()
            for row in range(self.row_count):
                cells.add(self.grid[row][col])
            # print(cells)  # check the cells being added
            self.check_len_cells(cells)

    def winner_exists(self) -> bool:
        if self._is_game_done is True:
            return True
        else:
            return False
    
    def win_tic_tac_toe(self):
        self.check_rows()
        self.check_cols()

    def win_not_connect_four(self):
        ...
    
    def winner_checker(self, player: Player):
        if self._win_con == WinConditionType.TIC_TAC_TOE:
            self.win_tic_tac_toe()
        else:
            ...

    def get_owner(self, row: int, col: int) -> Player | None:
        return self._grid[row][col] if self._grid[row][col] is not None else None
    

    # def winner_checker(self, player: Player):
    #     if self._win_con is WinConditionType.TIC_TAC_TOE:
    #         for row in range(self.row_count):
    #             cells: str = set()
    #             for col in range(self.col_count):
    #                 cells.add(self._grid[row][col])
    #             if len(cells) == 1:
    #                 self._winner = self.player
    #                 self._is_game_done = True

    #         for column in range(self.col_count):
    #             cells: str = set()
    #             for row in range(self.row_count):
    #                 cells.add(self._grid[row][col])
    #             if len(cells) == 1:
    #                 self._winner = self.player
    #                 self._is_game_done = True
                    
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
        # else:
        #     pass


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

    
