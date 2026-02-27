from argparse import ArgumentParser
from model import ConnectTacToeModel
from view import ConnectTacToeView
from common_types import Player

class ConnectTacToeController:
    def __init__(self, model: ConnectTacToeModel, view: ConnectTacToeView):
        self._model = model
        self._view = view

    def run(self):
        model = self._model
        view = self._view

        while not model.is_game_done:
            if model.current_player == Player.P1:
                ...
            else:
                ...
            ...

# if __name__ == "__main__":
#     model = ConnectTacToeModel()
