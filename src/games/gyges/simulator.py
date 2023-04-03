from src.games.gyges.player import GygesPlayer
from src.games.gyges.state import GygesState
from src.games.game_simulator import GameSimulator


class GygesSimulator(GameSimulator):

    def __init__(self, player1: GygesPlayer, player2: GygesPlayer, dimensions: int = 7):
        super(GygesSimulator, self).__init__([player1, player2])
        """
        the number of rows and cols from the TicTacToe grid
        """
        self.__num_rows = dimensions
        self.__num_cols = dimensions

    def init_game(self):
        return GygesState(self.__num_rows)

    def before_end_game(self, state: GygesState):
        # ignored for this simulator
        pass

    def end_game(self, state: GygesState):
        # ignored for this simulator
        pass
