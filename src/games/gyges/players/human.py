from src.games.gyges.action import GygesAction
from src.games.gyges.player import GygesPlayer
from src.games.gyges.state import GygesState


class HumanGygesPlayer(GygesPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: GygesState):
        state.display()
        while True:
            # noinspection PyBroadException
            try:
                # Se as peças estiverem todas colocadas
                if state.get_turn() > 12:
                    return GygesAction(int(input(f"Player {state.get_acting_player()}, choose a column: ")),
                                       int(input(f"Player {state.get_acting_player()}, choose a row: ")))
                else:
                    # O jogador 0 irá ficar com a parte de cima do tabuleiro
                    if state.get_acting_player() == 0:
                        return GygesAction(int(input(
                            f"Player {state.get_acting_player()}, choose the column where you want to put this piece: ")),
                                           1)
                    else:
                        # O jogador 1 irá ficar com a parte de baixo do tabuleiro
                        return GygesAction(int(input(
                            f"Player {state.get_acting_player()}, choose the column where you want to put this piece: ")),
                                           6)

            except Exception:
                continue

    def event_action(self, pos: int, action, new_state: GygesState):
        # ignore
        pass

    def event_end_game(self, final_state: GygesState):
        # ignore
        pass
