from random import randint

from src.games.gyges.action import GygesAction
from src.games.gyges.player import GygesPlayer
from src.games.gyges.state import GygesState
from src.games.state import State


"""Esta função retorna a lista com as peças da coluna mais próxima do jogador na forma (tipoPeça, coluna). 
O jogador irá utilizar as peças do tipo maior primeiro e só depois os tipos menores"""


def get_playable_pieces(state: GygesState, row: int):
    playable_pieces = []

    for c in range(0, state.get_num_cols()):
        if state.get_grid()[row][c] == 3:
            playable_pieces.append((state.get_grid()[row][c], c))

    for c in range(0, state.get_num_cols()):
        if state.get_grid()[row][c] == 2:
            playable_pieces.append((state.get_grid()[row][c], c))

    for c in range(0, state.get_num_cols()):
        if state.get_grid()[row][c] == 1:
            playable_pieces.append((state.get_grid()[row][c], c))

    return playable_pieces


class GreedyGygesPlayer(GygesPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: GygesState):
        while True:
            # noinspection PyBroadException
            try:

                option = 0
                ative_option1 = ative_option2 = ative_option3 = ative_option4 = False

                if state.get_turn() > 12:  # Se as peças estiverem todas colocadas

                    row = state.get_closest_playable_row()
                    pieces = get_playable_pieces(state, row)
                    col = pieces[0][1]

                    old_pos = [row, col]  # Posição anterior da peça
                    moves = state.get_grid()[row][col]  # O número de movimentos é igual ao tipo de peça escolhido

                    while moves != 0:  # Enquanto houver movimentos
                        can_move = False

                        while not can_move and len(pieces) != 0:

                            if state.get_acting_player() == 0:  # Apenas o jogador 0 pode mover a peça para baixo

                                """ Se a linha abaixo da peça for diferente da coluna 7 e estiver vazia ou só restar 1 
                                movimento Ou se a peça estiver nas colunas á beira da casa vencedora"""
                                if row + 1 != 7 and (state.get_grid()[row + 1][col] == -1 or
                                                     (state.get_grid()[row + 1][col] != -1 and moves == 1)) or\
                                   (row + 1 == 7 and 2 <= col <= 3 and moves == 1):

                                    ative_option1 = True
                                    can_move = True

                            """Se o ultimo movimento não foi para a direita e a coluna da esquerda estiver vazia
                            e diferente de 0 ou a coluna da esquerda estiver ocupada mas 
                            for o ultimo movimento da peça"""
                            if option != 3 and (col != 0 and (state.get_grid()[row][col - 1] == -1 or
                               (state.get_grid()[row][col - 1] != -1 and moves == 1))):

                                can_move = True
                                ative_option2 = True

                            """Se o ultimo movimento não foi para a esquerda e a coluna da esquerda estiver vazia
                            e diferente de 5 ou a coluna da direita estiver ocupada mas 
                            for o ultimo movimento da peça"""
                            if option != 2 and (col != 5 and (state.get_grid()[row][col + 1] == -1 or
                                                              (state.get_grid()[row][col + 1] != -1 and moves == 1))):

                                can_move = True
                                ative_option3 = True

                            if state.get_acting_player() == 1:  # Apenas o jogador 1 pode mover a peça para cima

                                """Se a linha acima da peça for diferente da coluna 0 e estiver vazia ou só restar 1 
                                movimento ou se a peça estiver nas colunas á beira da casa vencedora"""
                                if row - 1 != 0 and (state.get_grid()[row - 1][col] == -1 or
                                                     (state.get_grid()[row - 1][col] != -1 and moves == 1)) or\
                                   (row - 1 == 0 and 2 <= col <= 3 and moves == 1):

                                    can_move = True
                                    ative_option4 = True

                            # Se não conseguir mover a peça escolha a próxima peça na lista
                            if not can_move:

                                pieces.pop(0)
                                col = pieces[0][1]

                        if can_move:  # Se for possivel mover a peça

                            """O Greedy irá mover a peça para as colunas da casa de vitória (colunas 2 e 3) e de seguida
                            sempre que possivel, irá mover a peça para a frente. Caso não seja possivel, faz um 
                            movimento aleatorio"""

                            if col > 2 and ative_option2:
                                option = 2
                            elif col < 2 and ative_option3:
                                option = 3
                            elif ative_option1:
                                option = 1
                            elif ative_option4:
                                option = 4
                            else:
                                option = randint(1, 4)

                            # Se a opção escolhida for 1 e esta opção estiver disponivel
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

                            # Se a opção escolhida for 2 e esta opção estiver disponivel
                            elif option == 2 and ative_option2:
                                col -= 1

                                # Se calhar na casa de outra peça fica com os movimentos dessa peça
                                if state.get_grid()[row][col] != -1:
                                    moves += state.get_grid()[row][col]

                                # A nova posição fica com o valor da peça e a anterior fica vazia
                                state.get_grid()[row][col] = state.get_grid()[row][col + 1]
                                state.get_grid()[row][col + 1] = state.EMPTY_CELL

                            # Se a opção escolhida for 3 e esta opção estiver disponivel
                            elif option == 3 and ative_option3:
                                col += 1

                                # Se calhar na casa de outra peça fica com os movimentos dessa peça
                                if state.get_grid()[row][col] != -1:
                                    moves += state.get_grid()[row][col]

                                # A nova posição fica com o valor da peça e a anterior fica vazia
                                state.get_grid()[row][col] = state.get_grid()[row][col - 1]
                                state.get_grid()[row][col - 1] = state.EMPTY_CELL

                            # Se a opção escolhida for 4 e esta opção estiver disponivel
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

                            else:  # Se for selecionada uma opção que não seja possivel

                                moves += 1

                            ative_option1 = ative_option2 = ative_option3 = ative_option4 = False
                            moves -= 1

                        else:  # Se a peça não possa ser movida

                            # São colocados estes valores para que o validate_action retorne false
                            # E o jogador tenha outra hipótese
                            row = -1
                            col = -1
                            moves = 0

                    new_pos = [row, col]  # A nova posição da peça
                    return GygesAction(old_pos, new_pos)

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
