from random import choice
from src.games.gyges.action import GygesAction
from src.games.gyges.player import GygesPlayer
from src.games.gyges.state import GygesState
from src.games.state import State


class GreedyGygesPlayer(GygesPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: GygesState):
        grid = state.get_grid()

        selected_col = None
        selected_row = None
        max_count = 0

        for col in range(0, state.get_dimensions()):
            for row in range(0, state.get_dimensions()):
                if not state.validate_action(GygesAction(col, row)):
                    continue

                count = 0
                for r in range(0, state.get_dimensions()):
                    if grid[r][col] == self.get_current_pos():
                        count += 1

                for c in range(0, state.get_dimensions()):
                    if grid[row][c] == self.get_current_pos():
                        count += 1

                if row == col:
                    for i in range(0, state.get_dimensions()):
                        if grid[i][i] == self.get_current_pos():
                            count += 1

                if row + col == state.get_dimensions() - 1:
                    for i in range(0, state.get_dimensions()):
                        if grid[i][state.get_dimensions() - 1 - i] == self.get_current_pos():
                            count += 1

                # it swap the column if we exceed the count. if the count of chips is the same, we swap 50% of the times
                if selected_col is None or count > max_count or (count == max_count and choice([False, True])):
                    selected_col = col
                    selected_row = row
                    max_count = count

        if selected_col is None:
            raise Exception("There is no valid action")

        if selected_row is None:
            raise Exception("There is no valid action")

        return GygesAction(selected_col, selected_row)

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
