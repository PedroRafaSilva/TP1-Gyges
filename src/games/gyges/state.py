from typing import Optional

from src.games.gyges.action import GygesAction
from src.games.gyges.result import GygesResult
from src.games.state import State


class GygesState(State):
    EMPTY_CELL = -1

    def __init__(self, col: int, row: int):
        super().__init__()

        """
        the dimensions of the board
        """
        self.__dimensions = row
        self.__num_rows = row
        self.__num_cols = col

        """
        the grid
        """
        self.__grid = [[GygesState.EMPTY_CELL for _i in range(self.__num_cols)] for _j in range(self.__num_rows)]

        """
        counts the number of turns in the current game
        """
        self.__turns_count = 1

        """
        the index of the current acting player
        """
        self.__acting_player = 0

        """
        determine if a winner was found already 
        """
        self.__has_winner = False

    def __check_winner(self, player):
        # check for 3 acroos
        for row in range(0, self.__num_rows):
            for col in range(0, self.__num_cols - 2):
                if self.__grid[row][col] == player and \
                        self.__grid[row][col + 1] == player and \
                        self.__grid[row][col + 2] == player:
                    return True

        # check for 3 up and down
        for row in range(0, self.__num_rows - 2):
            for col in range(0, self.__num_cols):
                if self.__grid[row][col] == player and \
                        self.__grid[row + 1][col] == player and \
                        self.__grid[row + 2][col] == player:
                    return True

        # check upward diagonal
        for row in range(2, self.__num_rows):
            for col in range(0, self.__num_cols - 2):
                if self.__grid[row][col] == player and \
                        self.__grid[row - 1][col + 1] == player and \
                        self.__grid[row - 2][col + 2] == player:
                    return True

        # check downward diagonal
        for row in range(0, self.__num_rows - 2):
            for col in range(0, self.__num_cols - 2):
                if self.__grid[row][col] == player and \
                        self.__grid[row + 1][col + 1] == player and \
                        self.__grid[row + 2][col + 2] == player:
                    return True

        return False

    def get_grid(self):
        return self.__grid

    def get_num_players(self):
        return 2

    def validate_action(self, action: GygesAction) -> bool:
        col = action.get_col()
        row = action.get_row()

        # valid column
        if col < 0 or col >= self.__num_cols:
            return False

        if row < 0 or row >= self.__num_rows:
            return False

        # full column
        if self.__grid[row][col] != GygesState.EMPTY_CELL:
            return False

        return True

    def update(self, action: GygesAction):
        col = action.get_col()
        row = action.get_row()

        self.__grid[row][col] = self.__acting_player

        # determine if there is a winner
        self.__has_winner = self.__check_winner(self.__acting_player)

        # switch to next player
        self.__acting_player = 1 if self.__acting_player == 0 else 0

        self.__turns_count += 1

    def __display_cell(self, row, col):
        print({
                  0: ' X ',
                  1: ' O ',
                  GygesState.EMPTY_CELL: ' x '
              }[self.__grid[row][col]], end="")

    def __display_numbers(self):
        for col in range(0, self.__num_cols):
            print(" " + str(col) + " ", end="")
            if col == self.__num_cols:
                print(" " + str(col) + " ")
        print("")

    def __display_separator(self):
        for col in range(0, self.__num_cols):
            print("----", end="")
        print("-")



    def display(self):
        # tela do jogo
        self.__display_numbers()
        for row in range(0, self.__num_rows):
            for col in range(0, self.__num_cols):
                if row == 0 or row == 7:
                    print("  ", end="")
                    if col == 2:
                        print("\t", end="")
                        self.__display_cell(row, col)
                else:
                    self.__display_cell(row, col)
            print("\t" + str(row))





    def __is_full(self):
        return self.__turns_count > (self.__num_cols * self.__num_rows)

    def is_finished(self) -> bool:
        return self.__has_winner or self.__is_full()

    def get_acting_player(self) -> int:
        return self.__acting_player

    def clone(self):
        cloned_state = GygesState(self.__num_cols, self.__num_rows)
        cloned_state.__turns_count = self.__turns_count
        cloned_state.__acting_player = self.__acting_player
        cloned_state.__has_winner = self.__has_winner
        for row in range(0, self.__num_rows):
            for col in range(0, self.__num_cols):
                cloned_state.__grid[row][col] = self.__grid[row][col]
        return cloned_state

    def get_result(self, pos) -> Optional[GygesResult]:
        if self.__has_winner:
            return GygesResult.LOOSE if pos == self.__acting_player else GygesResult.WIN
        if self.__is_full():
            return GygesResult.DRAW
        return None

    def get_num_rows(self):
        return self.__num_rows

    def get_num_cols(self):
        return self.__num_cols

    def get_dimensions(self):
        return self.__dimensions

    def before_results(self):
        pass

    def get_possible_actions(self):
        return list(filter(
            lambda action: self.validate_action(action),
            map(
                lambda pos: GygesAction(pos[0], pos[1]),
                [(i, j) for i in range(self.get_dimensions()) for j in range(self.get_dimensions())]
            )
        ))

    def sim_play(self, action):
        new_state = self.clone()
        new_state.play(action)
        return new_state
