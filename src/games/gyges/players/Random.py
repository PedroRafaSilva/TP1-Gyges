from random import randint

from src.games.gyges.action import GygesAction
from src.games.gyges.player import GygesPlayer
from src.games.gyges.state import GygesState
from src.games.state import State


class RandomGygesPlayer(GygesPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: GygesState):
        return GygesAction(randint(0, state.get_num_rows()), randint(0, state.get_num_cols()))

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
