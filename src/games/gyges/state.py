from typing import Optional

from games.gyges.piece import Piece
from src.games.gyges.action import GygesAction
from src.games.gyges.result import GygesResult
from src.games.state import State

"""
Esta classe tem as cores para personalizar o output (como o tabuleiro, por exemplo)
"""


class Color:
    PINK = '\033[1;35;48m'
    CYAN = '\033[1;36;48m'
    BOLD = '\033[1;37;48m'
    BLUE = '\033[1;34;48m'
    GREEN = '\033[1;32;48m'
    YELLOW = '\033[1;33;48m'
    RED = '\033[1;31;48m'
    BLACK = '\033[1;30;48m'
    UNDERLINE = '\033[4;37;48m'
    END = '\033[1;37;0m'


class GygesState(State):
    EMPTY_CELL = -1

    def __init__(self, col: int, row: int):
        super().__init__()

        """
        As peças do jogo
        """
        self.__pieces = [Piece(1), Piece(1), Piece(2), Piece(2), Piece(3), Piece(3),
                         Piece(1), Piece(1), Piece(2), Piece(2), Piece(3), Piece(3)]

        """
        the dimensions of the board
        """
        self.__num_rows = row
        self.__num_cols = col

        """
        Numero de jogadas sem se mover
        """
        self.cannot_move100 = 0

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

    """
    Esta função retorna a linha com peças mais próxima do jogador
    """
    def get_closest_playable_row(self):
        if self.__acting_player == 0:
            for row in range(0, self.__num_rows):
                for col in range(0, self.__num_cols):
                    if self.__grid[row][col] != -1:
                        return row
        if self.__acting_player == 1:
            for row in reversed(range(0, self.__num_rows)):
                for col in range(0, self.__num_cols):
                    if self.__grid[row][col] != -1:
                        return row

    """
    Retorna o nº do turno
    """
    def get_turn(self):
        return self.__turns_count

    """
    Verifica se o jogo já começou
    O jogo só começa quando todas as peças estão no tabuleiro
    """
    def start_game(self):
        if self.__pieces:
            return False
        return True

    """
    Verifica se há algum vencedor, caso a casa (7, 2) ou (0, 2) não estejam vazias, existe vencedor
    """
    def __check_winner(self):
        if self.__grid[7][2] != -1 or self.__grid[0][2] != -1:
            return True
        return False

    """
    Retorna o tabuleiro
    """
    def get_grid(self):
        return self.__grid

    """
    Retorna o numero de jogadores
    """
    def get_num_players(self):
        return 2

    """
    Esta função serve para validar cada jogada.
    Se a jogada for contra as regras do jogo, retorna falso.
    Caso contrário, retorna verdadeiro.
    Normalmente, antecede a função update.
    """
    def validate_action(self, action: GygesAction) -> bool:
        if not self.start_game():
            """
            Dar valor as variaveis que vao ser usadas
            """
            col = action.get_col()
            row = action.get_row()
        else:
            """
            Verifica a nova posição da peça
            """
            col = action.get_col()[1]
            row = action.get_col()[0]

        """
        Se o jogador estiver bloqueado muda de jogador
        """
        self.cannot_move100 += 1
        if self.cannot_move100 == 100:
            self.cannot_move100 = 0
            self.__acting_player = 1 if self.__acting_player == 0 else 0

        """
        verificar se a posição da peça está certa
        """
        if col < 0 or col > self.__num_cols:
            return False

        if row < 0 or row > self.__num_rows:
            return False

        if self.__grid[row][col] != GygesState.EMPTY_CELL and not self.start_game():
            return False

        return True

    """
    Esta função irá atualizar o tabuleiro na colocação das peças e durante o jogo, após uma jogada
    """
    def update(self, action: GygesAction):
        col = action.get_col()
        row = action.get_row()

        """
        Enquanto o jogo não começa, vai-se colocando as peças no tabuleiro
        """
        if not self.start_game():
            self.__grid[row][col] = self.__pieces[0].get_piece_type()
            self.__pieces.pop(0)

        else:
            """
            Coloca a peça na sua nova posição
            A nova posição da peça fica com a posição antiga
            """
            self.__grid[col[0]][col[1]] = self.__grid[row[0]][row[1]]
            self.__grid[row[0]][row[1]] = self.EMPTY_CELL

        """
        Determine if there is a winner
        """
        self.__has_winner = self.__check_winner()

        """
        switch to next player
        """
        self.__acting_player = 1 if self.__acting_player == 0 else 0

        self.__turns_count += 1

    """
    Mostra os valores das peças dependendo do tipo 1, 2 ou 3
    """
    def __display_cell(self, row, col):
        print({
                  1: Color.GREEN + '| 1 ' + Color.END,
                  2: Color.BLUE + '| 2 ' + Color.END,
                  3: Color.YELLOW + '| 3 ' + Color.END,
                  GygesState.EMPTY_CELL: '| _ '
              }[self.__grid[row][col]], end="")

    """
    Mostra os valores das linhas e das colunas
    """
    def __display_numbers(self):
        print(Color.PINK + "|   ", end="")
        for col in range(0, self.__num_cols):
            print("| " + str(col) + " ", end="")
            if col == self.__num_cols:
                print(str(col) + " | ")
        print("|   |" + Color.END)

    """
    Cria um seprador
    """
    def __display_separator(self):
        for col in range(0, self.__num_cols):
            print("----", end="")
        print("-")

    """
    Cria o tabuleiro, que pode ser visto na consola
    """
    def display(self):
        self.__display_numbers()
        for row in range(0, self.__num_rows):
            print(Color.PINK + "| " + str(row) + " " + Color.END, end="")
            for col in range(0, self.__num_cols):
                if row == 0 or row == 7:
                    if col == 0:
                        print(Color.CYAN + "| ", end="")
                    print("__", end="")
                    if col == 2:
                        print("__", end="")
                        self.__display_cell(row, col)
                        print("|__", end="")
                    if col == 5:
                        print(" " + Color.END, end="")
                else:
                    self.__display_cell(row, col)
            print(Color.PINK + "| " + str(row) + " |" + Color.END)
        self.__display_numbers()

        """
        Mostra o tipo da peça a colocar no tabuleiro
        """
        if self.__turns_count < 12:
            print("Piece type: " + str(self.__pieces[self.__turns_count - 1].get_piece_type()))

    """ # Board Inicial
    - A - B - C - D - E - F -
    __________| w |__________ A
    | _ | 2 | 3 | 4 | 5 | 6 | B 
    | 1 | 2 | 3 | 4 | 5 | 6 | C 
    | 1 | 2 | 3 | 4 | 5 | 6 | D
    | 1 | 2 | 3 | 4 | 5 | 6 | E
    | 1 | 2 | 3 | 4 | 5 | 6 | F
    | 1 | 2 | 3 | 4 | 5 | 6 | G
    __________| w |__________ H
    
    nivel 1 -> 1
    nivel 2 -> 2
    nivel 3 -> 3
    vazio -> _
    impossible -> X
    
    """

    """
    Verifica se o tabuleiro está cheio (não é usado)
    """
    def __is_full(self):
        return self.__turns_count > (self.__num_cols * self.__num_rows)

    """
    verificar se o jogo está acabado ou não
    """
    def is_finished(self) -> bool:
        return self.__has_winner

    """
    Retorna o jogador que está a jogar naquele turno
    """
    def get_acting_player(self) -> int:
        return self.__acting_player

    """
    Esta função cria um clone do estado atual
    Isto é utilizado, para realizar testes de movimentos, como no caso do minimax
    """
    def clone(self):
        cloned_state = GygesState(self.__num_cols, self.__num_rows)
        cloned_state.__turns_count = self.__turns_count
        cloned_state.__acting_player = self.__acting_player
        cloned_state.__has_winner = self.__has_winner
        """
        O estado clonado tem o conjunto de peças cheio, por isso verifica se o jogo já começou e se tal for verdade
        fica com o valor do conjunto das peças do estado original (que é [](vazio))
        """
        if self.start_game():
            cloned_state.__pieces = self.__pieces
        for row in range(0, self.__num_rows):
            for col in range(0, self.__num_cols):
                cloned_state.__grid[row][col] = self.__grid[row][col]
        return cloned_state

    """
    Retorna o resultado do jogo caso haja um vencedor
    """
    def get_result(self, pos) -> Optional[GygesResult]:
        if self.__has_winner:
            return GygesResult.LOOSE if pos == self.__acting_player else GygesResult.WIN

    """
    Retorna o número de linhas do tabuleiro
    """
    def get_num_rows(self):
        return self.__num_rows

    """
    Retorna o número de colunas do tabuleiro
    """
    def get_num_cols(self):
        return self.__num_cols

    def before_results(self):
        pass

    """
    Retorna a lista de todas as jogadas possiveis(não utilizado)
    """
    def get_possible_actions(self):
        return list(filter(
            lambda action: self.validate_action(action),
            map(
                lambda pos: GygesAction(pos[0], pos[1]),
                [(i, j) for i in range(1, self.get_num_rows()) for j in range(self.get_num_cols())]
            )
        ))

    """
    Simula uma jogada
    """
    def sim_play(self, action):
        new_state = self.clone()
        new_state.play(action)
        return new_state
