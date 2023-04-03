from typing import Optional

from src.games.gyges.action import GygesAction
from src.games.gyges.result import GygesResult
from src.games.state import State


class GygesState(State):
    EMPTY_CELL = -1

    def __init__(self, dimensions: int):
        super().__init__()

        if dimensions < 3:
            raise Exception("the dimensions of the board must be 3 or over")

        """
        the dimensions of the board
        """
        self.__dimensions = dimensions
        self.__num_rows = dimensions
        self.__num_cols = dimensions

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
                  0: 'X',
                  1: 'O',
                  GygesState.EMPTY_CELL: ' '
              }[self.__grid[row][col]], end="")

    def __display_numbers(self):
        for col in range(0, self.__num_cols):
            print(str(col) + "\t", end="")
        print("")

    def __display_separator(self):
        for col in range(0, self.__num_cols):
            print("---", end="")
        print("---")



    def display(self):
        # tela do jogo
        width = self.__num_rows
        height = self.__num_cols

        # Print do tabuleiro de xadrez
        print('\033[1;35m_____________________________________')
        print('|   | ', end='')

        # Legenda Topo (coluna)
        for i in range(width):
            print(str(i) + ' | ', end='')

        print('\n-------------------------------------\033[1;0m')

        # Tabuleiro + Legenda Esquerda
        for i in range(height):

            # Legenda da linha
            print('\033[1;35m' + '| ' + str(i) + ' |', end='')

            # Linhas do Tabuleiro
            for x in range(width):
                print('\033[1;0m ', end='')

                if self.__grid[i][x] == 0:
                    print(' ', end='')
                elif self.__grid[i][x] == 2:
                    print('\033[1;33mW', end='')
                elif self.__grid[i][x] == 1:
                    print('\033[1;36mB', end='')

                print('\033[1;0m |', end='')

            print()

        # Muda de linha
        print('-------------------------------------')
        """self.__display_numbers()
        for row in range(0, self.__num_rows):
            for col in range(0, self.__num_cols):
                self.__display_cell(row, col)
                if col != self.__num_cols - 1:
                    print(' | ', end="")
            print("\t" + str(row))
            if row != self.__num_rows - 1:
                self.__display_separator()
        print("\n")"""

    def __is_full(self):
        return self.__turns_count > (self.__num_cols * self.__num_rows)

    def is_finished(self) -> bool:
        return self.__has_winner or self.__is_full()

    def get_acting_player(self) -> int:
        return self.__acting_player

    def clone(self):
        cloned_state = GygesState(self.__num_rows)
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
