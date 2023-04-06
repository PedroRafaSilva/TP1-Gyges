from src.games.gyges.action import GygesAction
from src.games.gyges.player import GygesPlayer
from src.games.gyges.state import GygesState


class HumanGygesPlayer(GygesPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: GygesState):
        state.display2()
        while True:
            # noinspection PyBroadException
            try:
                return GygesAction(int(input(f"Player {state.get_acting_player()}, choose a column: ")),
                                       int(input(f"Player {state.get_acting_player()}, choose a row: ")))
            except Exception:
                continue

    def event_action(self, pos: int, action, new_state: GygesState):
        # ignore
        pass

    def event_end_game(self, final_state: GygesState):
        # ignore
        pass
