from random import randint

from src.games.gyges.action import GygesAction
from src.games.gyges.player import GygesPlayer
from src.games.gyges.state import GygesState
from src.games.state import State


class RandomGygesPlayer(GygesPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: GygesState):
        while True:
            # noinspection PyBroadException
            try:
                op = row = col = 0
                proceed = False
                ative1 = ative2 = ative3 = ative4 = False
                if state.get_turn() > 12:  # Se as peças estiverem todas colocadas
                    while not proceed:  # Enqaunto não for escolhida a/as peça(s) mais próxima(s)
                        row = randint(1, 6)
                        col = randint(0, 5)

                        # Se o jogador 0 escolher o campo com uma peça mais próxima dele, continua
                        if state.get_acting_player() == 0 and row == state.get_closest_piece() and state.get_grid()[row][col] != -1:
                            proceed = True

                        # Se o jogador 1 escolher o campo com uma peça mais próxima dele, continua
                        elif state.get_acting_player() == 1 and row == state.get_away_piece() and state.get_grid()[row][col] != -1:
                            proceed = True

                        # Caso contrário volta a escolher a linha e a coluna da peça a jogar
                        else:
                            proceed = False

                    old_pos = [row, col]  # Posição anterior da peça
                    moves = state.get_grid()[row][col]  # O nº de movimentos é igual ao tipo de peça escolhido

                    while moves != 0:  # Enquanto houver movimentos
                        can_move = False
                        if state.get_acting_player() == 0:  # Apenas o jogador 0 pode mover a peça para baixo
                            # Se a linha abaixo da peça for diferente da coluna 7 e estiver vazia ou só restar 1 movimento
                            # Ou se a peça estiver nas colunas á beira da casa vencedora
                            if row + 1 != 7 and (state.get_grid()[row + 1][col] == -1 or (state.get_grid()[row + 1][col] != -1 and moves == 1)) or\
                               (row + 1 == 7 and 2 <= col <= 3 and moves == 1):
                                ative1 = True
                                can_move = True

                        # Se o ultimo movimento não foi para a direita e a coluna da esquerda estiver vazia
                        # e diferente de 0 ou a coluna da esquerda estiver ocupada mas for o ultimo movimento da peça
                        if op != 3 and (col != 0 and (state.get_grid()[row][col - 1] == -1 or
                           (state.get_grid()[row][col - 1] != -1 and moves == 1))):
                            can_move = True
                            ative2 = True

                        # Se o ultimo movimento não foi para a esquerda e a coluna da esquerda estiver vazia
                        # e diferente de 5 ou a coluna da direita estiver ocupada mas for o ultimo movimento da peça
                        if op != 2 and (col != 5 and (state.get_grid()[row][col + 1] == -1 or (state.get_grid()[row][col + 1] != -1 and moves == 1))):
                            can_move = True
                            ative3 = True

                        if state.get_acting_player() == 1:  # Apenas o jogador 1 pode mover a peça para cima
                            # Se a linha acima da peça for diferente da coluna 0 e estiver vazia ou só restar 1 movimento
                            # Ou se a peça estiver nas colunas á beira da casa vencedora
                            if row - 1 != 0 and (state.get_grid()[row - 1][col] == -1 or (state.get_grid()[row - 1][col] != -1 and moves == 1)) or\
                               (row - 1 == 0 and 2 <= col <= 3 and moves == 1):
                                can_move = True
                                ative4 = True

                        if can_move:  # Se for possivel mover a peça

                            op = randint(1, 4)

                            if op == 1 and ative1:  # Se a opção escolhida for 1 e esta opção estiver disponivel
                                if row == 6 and col == 3:  # Permite o jogador aceder á casa vencedora através da col 3
                                    col -= 1
                                row += 1
                                # Se calhar na casa de outra peça fica com os movimentos dessa peça
                                if state.get_grid()[row][col] != -1:
                                    moves += state.get_grid()[row][col]
                                # A nova posição fica com o valor da peça e a anterior fica vazia
                                state.get_grid()[row][col] = state.get_grid()[row - 1][col]
                                state.get_grid()[row - 1][col] = state.EMPTY_CELL


                            elif op == 2 and ative2:  # Se a opção escolhida for 2 e esta opção estiver disponivel
                                col -= 1
                                # Se calhar na casa de outra peça fica com os movimentos dessa peça
                                if state.get_grid()[row][col] != -1:
                                    moves += state.get_grid()[row][col]
                                # A nova posição fica com o valor da peça e a anterior fica vazia
                                state.get_grid()[row][col] = state.get_grid()[row][col + 1]
                                state.get_grid()[row][col + 1] = state.EMPTY_CELL


                            elif op == 3 and ative3:  # Se a opção escolhida for 3 e esta opção estiver disponivel
                                col += 1
                                # Se calhar na casa de outra peça fica com os movimentos dessa peça
                                if state.get_grid()[row][col] != -1:
                                    moves += state.get_grid()[row][col]
                                # A nova posição fica com o valor da peça e a anterior fica vazia
                                state.get_grid()[row][col] = state.get_grid()[row][col - 1]
                                state.get_grid()[row][col - 1] = state.EMPTY_CELL


                            elif op == 4 and ative4:  # Se a opção escolhida for 4 e esta opção estiver disponivel
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

                            ative1 = ative2 = ative3 = ative4 = False
                            moves -= 1

                        else:  # Se a peça não possa ser movida

                            # São colocados este valores para que o validate_action retorne false
                            # E o jogador tenha outra chance
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
