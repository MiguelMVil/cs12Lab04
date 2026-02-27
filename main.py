from argparse import ArgumentParser
from model import ConnectTacToeModel
from view import ConnectTacToeView
from common_types import Player, WinConditionType, TokenPhysicsType

class ConnectTacToeController:
    def __init__(self, model: ConnectTacToeModel, view: ConnectTacToeView):
        self._model = model
        self._view = view

    def run(self):
        model = self._model
        view = self._view

        while not model.is_game_done:
            if model.current_player == Player.P1:
                view.print_player(model.current_player)
                view.print_grid(model.grid)
                i, j = view.get_input()
                while model.choose_cell(i - 1, j - 1) is False:
                    i, j = view.get_input(True)

                model.elapse_player_turn()
            else:
                view.print_player(model.current_player)
                view.print_grid(model.grid)
                i, j = view.get_input()
                while model.choose_cell(i - 1, j - 1) is False:
                    i, j = view.get_input(True)
                model.elapse_player_turn()
            view.print_winner(model.current_player)

if __name__ == "__main__":
    model = ConnectTacToeModel(WinConditionType.TIC_TAC_TOE, 
                               TokenPhysicsType.FLOATING)
    view = ConnectTacToeView()
    controller = ConnectTacToeController(model, view)

    controller.run()
