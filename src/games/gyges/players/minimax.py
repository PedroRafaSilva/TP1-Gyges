import math
from random import randint

from games.gyges.action import GygesAction
from src.games.gyges.player import GygesPlayer
from src.games.gyges.result import GygesResult
from src.games.gyges.state import GygesState
from src.games.state import State

""""
Esta função retorna as peças que o jogador pode mover
"""


def get_playable_pieces(state: GygesState):
    playable_pieces = []
    row = state.get_closest_playable_row()

    for col in range(0, state.get_num_cols()):
        if state.get_grid()[row][col] != -1:
            playable_pieces.append((row, col))

    return playable_pieces


"""
Esta função retorna os movimentos de uma peça
"""


def get_moves(state: GygesState, row, col):
    option = 0
    ative_option1 = ative_option2 = ative_option3 = ative_option4 = False
    old_pos = [row, col]  # Posição anterior da peça
    moves = state.get_grid()[row][col]  # O número de movimentos é igual ao tipo de peça escolhido

    while moves != 0:  # Enquanto houver movimentos
        can_move = False

        if state.get_acting_player() == 0:  # Apenas o jogador 0 pode mover a peça para baixo

            """Se a linha abaixo da peça for diferente da coluna 7 e estiver vazia ou só restar 1 
            movimento Ou se a peça estiver nas colunas á beira da casa vencedora"""
            if row + 1 != 7 and (state.get_grid()[row + 1][col] == -1 or (
                    state.get_grid()[row + 1][col] != -1 and moves == 1)) or \
                    (row + 1 == 7 and 2 <= col <= 3 and moves == 1):

                ative_option1 = True
                can_move = True

        """Se o ultimo movimento não foi para a direita e a coluna da esquerda estiver vazia
        e diferente de 0 ou a coluna da esquerda estiver ocupada mas for o ultimo movimento da peça"""
        if option != 3 and (col != 0 and (state.get_grid()[row][col - 1] == -1 or
                                          (state.get_grid()[row][col - 1] != -1 and moves == 1))):

            can_move = True
            ative_option2 = True

        """Se o ultimo movimento não foi para a esquerda e a coluna da esquerda estiver vazia
        e diferente de 5 ou a coluna da direita estiver ocupada mas for o ultimo movimento da peça"""
        if option != 2 and (col != 5 and (state.get_grid()[row][col + 1] == -1 or (
                state.get_grid()[row][col + 1] != -1 and moves == 1))):

            can_move = True
            ative_option3 = True

        if state.get_acting_player() == 1:  # Apenas o jogador 1 pode mover a peça para cima

            """Se a linha acima da peça for diferente da coluna 0 e estiver vazia ou só restar 1 
            movimento Ou se a peça estiver nas colunas á beira da casa vencedora"""
            if row - 1 != 0 and (state.get_grid()[row - 1][col] == -1 or (
                    state.get_grid()[row - 1][col] != -1 and moves == 1)) or \
                    (row - 1 == 0 and 2 <= col <= 3 and moves == 1):

                can_move = True
                ative_option4 = True

        if can_move:  # Se for possivel mover a peça

            """"
            Por vezes, algumas jogadas são repetidas.
            Por exemplo, o jogador 0, jogava a peça mais perto e depois essa peça passava a ser a peça mais perto
            do jogador 1 e ficavam sempre a mover a mesma peça infinitamente.
            Ao escolher um movimento aleatório, o jogo continua.
            A condição garante que a cada turno divisivel por 250, isso acontece.
            Foi escolhido este número para evitar problemas com outras jogadas melhores, 
            uma vez que um jogo raramente tem mais que 250 movimentos.
            """
            if state.get_turn() % 250 == 0:
                option = randint(1, 4)

            elif col > 2 and ative_option2:
                option = 2
            elif col < 2 and ative_option3:
                option = 3
            elif ative_option1:
                option = 1
            elif ative_option4:
                option = 4
            else:
                option = randint(1, 4)

            # Se a optionção escolhida for 1 e esta opção estiver disponivel
            if option == 1 and ative_option1:

                if row == 6 and col == 3:  # Permite o jogador aceder á casa vencedora através da col 3
                    col -= 1

                row += 1
                # Se calhar na casa de outra peça fica com os movimentos dessa peça
                if state.get_grid()[row][col] != -1:
                    moves += state.get_grid()[row][col]

                # A nova posição fica com o valor da peça e a anterior fica vazia
                state.get_grid()[row][col] = state.get_grid()[row - 1][col]
                state.get_grid()[row - 1][col] = state.EMPTY_CELL

            # Se a optionção escolhida for 2 e esta opção estiver disponivel
            elif option == 2 and ative_option2:
                col -= 1

                # Se calhar na casa de outra peça fica com os movimentos dessa peça
                if state.get_grid()[row][col] != -1:
                    moves += state.get_grid()[row][col]

                # A nova posição fica com o valor da peça e a anterior fica vazia
                state.get_grid()[row][col] = state.get_grid()[row][col + 1]
                state.get_grid()[row][col + 1] = state.EMPTY_CELL

            # Se a optionção escolhida for 3 e esta opção estiver disponivel
            elif option == 3 and ative_option3:
                col += 1

                # Se calhar na casa de outra peça fica com os movimentos dessa peça
                if state.get_grid()[row][col] != -1:
                    moves += state.get_grid()[row][col]

                # A nova posição fica com o valor da peça e a anterior fica vazia
                state.get_grid()[row][col] = state.get_grid()[row][col - 1]
                state.get_grid()[row][col - 1] = state.EMPTY_CELL

            # Se a optionção escolhida for 4 e esta opção estiver disponivel
            elif option == 4 and ative_option4:

                if row == 1 and col == 3:  # Permite o jogador aceder á casa vencedora através da col 3
                    col -= 1

                row -= 1
                # Se calhar na casa de outra peça fica com os movimentos dessa peça
                if state.get_grid()[row][col] != -1:
                    moves += state.get_grid()[row][col]

                # A nova posição fica com o valor da peça e a anterior fica vazia
                state.get_grid()[row][col] = state.get_grid()[row + 1][col]
                state.get_grid()[row + 1][col] = state.EMPTY_CELL

            else:  # Se for selecionada uma optionção que não seja possivel
                moves += 1

            ative_option1 = ative_option2 = ative_option3 = ative_option4 = False
            moves -= 1

        else:  # Se a peça não possa ser movida

            moves = 0

    new_pos = [row, col]  # A nova posição da peça

    return old_pos, new_pos


"""
Esta função retorna todos os movimentos das peças que o jogador pode utilizar
"""


def get_available_moves(state: GygesState):
    all_movements = []

    for piece in get_playable_pieces(state):
        cloned_state = state.clone()
        all_movements.append(get_moves(cloned_state, piece[0], piece[1]))

    return all_movements


"""
Esta função realiza um movimento e retorna o estado do jogo após o movimento
"""


def make_move(state: GygesState, move):
    cloned_state = state.clone()
    move = GygesAction(move[0], move[1])

    if cloned_state.validate_action(move):
        cloned_state.update(move)

    return cloned_state


class MinimaxGygesPlayer(GygesPlayer):

    def __init__(self, name):
        super().__init__(name)

    """
    Esta função retorna um valor do estado do jogo
    """

    def evaluate_state(self, state: GygesState):
        # Check if the game is over
        if state.is_finished():
            return {
                GygesResult.WIN: 40,
                GygesResult.LOOSE: -40,
            }[state.get_result(self.get_current_pos())]
        else:
            """
            O valor do estado do jogo será maior, quento mais perto as peças do jogador estiverem da casa de vitória
            """
            distance = 0
            if state.get_acting_player() == 0:
                row = state.get_closest_playable_row()
                for col in range(0, state.get_num_cols()):
                    if state.get_grid()[row][col] != -1:
                        distance += abs(7 - row) + abs(2 - col)
            else:
                """
                 O valor do estado do jogo será menor, quento mais perto as peças do jogador adversário
                 estiverem da casa de vitória
                """
                row = state.get_closest_playable_row()
                for col in range(0, state.get_num_cols()):
                    if state.get_grid()[row][col] != -1:
                        distance -= abs(0 - row) + abs(2 - col)
        return distance

    def minimax(self, state: GygesState, depth: int, alpha: int = -math.inf, beta: int = math.inf,
                is_initial_node: bool = True):
        # first we check if we are in a terminal node (victory, draw or loose)
        if state.is_finished():
            return {
                GygesResult.WIN: 40,
                GygesResult.LOOSE: -40
            }[state.get_result(self.get_current_pos())]

        # if we reached the maximum depth, we will return the value of the heuristic
        if depth == 0:
            return self.evaluate_state(state)

        # if we are the acting player
        if self.get_current_pos() == state.get_acting_player():
            # very small integer
            value = -math.inf
            selected_action = None

            for action in get_available_moves(state):
                pre_value = value
                value = max(value, self.minimax(make_move(state, action), depth - 1, alpha, beta, False))
                if value > pre_value:
                    selected_action = action
                if value > beta:
                    break
                alpha = max(alpha, value)

            return selected_action if is_initial_node else value

        # if it is the opponent's turn
        else:
            value = math.inf
            for action in get_available_moves(state):
                value = min(value, self.minimax(make_move(state, action), depth - 1, alpha, beta, False))
                if value < alpha:
                    break
                beta = min(beta, value)

            return value

    def get_action(self, state: GygesState):
        while True:
            # noinspection PyBroadException
            try:
                if state.get_turn() > 12:

                    return GygesAction(self.minimax(state, 3)[0], self.minimax(state, 3)[1])

                else:

                    # O jogador 0 irá ficar com a parte de cima do tabuleiro
                    if state.get_acting_player() == 0:

                        return GygesAction(1, randint(0, 5))

                    else:

                        # O jogador 1 irá ficar com a parte de baixo do tabuleiro
                        return GygesAction(6, randint(0, 5))

            except Exception:
                continue

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
