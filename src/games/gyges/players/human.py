
from src.games.gyges.action import GygesAction
from src.games.gyges.player import GygesPlayer
from src.games.gyges.state import GygesState, color


class HumanGygesPlayer(GygesPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: GygesState):
        state.display()
        while True:
            # noinspection PyBroadException
            try:
                op = row = col = 0
                proceed = False
                can_move = False
                ative1 = ative2 = ative3 = ative4 = False
                if state.get_turn() > 12:  # Se as peças estiverem todas colocadas

                    while not proceed:  # Enqaunto não for escolhida a/as peça(s) mais próxima(s)
                        print("\nInsert the positions of a piece, " + color.YELLOW + f"Player {state.get_acting_player()}" + color.END)
                        row = int(input("Choose the row of the piece: "))
                        col = int(input("Choose the column of the piece: "))

                        # Se o jogador 0 escolher o campo com uma peça mais próxima dele, continua
                        if state.get_acting_player() == 0 and row == state.get_closest_piece() and state.get_grid()[row][col] != -1:
                            proceed = True

                        # Se o jogador 1 escolher o campo com uma peça mais próxima dele, continua
                        elif state.get_acting_player() == 1 and row == state.get_away_piece() and state.get_grid()[row][col] != -1:
                            proceed = True

                        # Caso contrário volta a escolher a linha e a coluna da peça a jogar
                        else:
                            proceed = False
                            print(color.RED + "Choose a piece that is closest to you!!!" + color.END)
                            state.display()

                    old_pos = [row, col]  # Posição anterior da peça
                    moves = state.get_grid()[row][col]  # O nº de movimentos é igual ao tipo de peça escolhido

                    while moves != 0:  # Enquanto houver movimentos
                        print("\nMovimentos")
                        if state.get_acting_player() == 0:  # Apenas o jogador 0 pode mover a peça para baixo
                            # Se a linha abaixo da peça for diferente da coluna 7 e estiver vazia ou só restar 1 movimento
                            # Ou se a peça estiver nas colunas á beira da casa vencedora
                            if row + 1 != 7 and (state.get_grid()[row + 1][col] == -1 or moves == 1) or row + 1 == 7 and 2 <= col <= 3:
                                print("1 - Para baixo")
                                ative1 = True
                                can_move = True

                        # Se o ultimo movimento não foi para a direita e a coluna da esquerda estiver vazia
                        # e diferente de 0 ou a coluna da esquerda estiver ocupada mas for o ultimo movimento da peça
                        if op != 3 and col != 0 and (state.get_grid()[row][col - 1] == -1 or moves == 1):
                            print("2 - Para a esquerda")
                            can_move = True
                            ative2 = True

                        # Se o ultimo movimento não foi para a esquerda e a coluna da esquerda estiver vazia
                        # e diferente de 5 ou a coluna da direita estiver ocupada mas for o ultimo movimento da peça
                        if op != 2 and col != 5 and (state.get_grid()[row][col + 1] == -1 or moves == 1):
                            print("3 - Para a direita")
                            can_move = True
                            ative3 = True

                        if state.get_acting_player() == 1:  # Apenas o jogador 1 pode mover a peça para cima
                            # Se a linha acima da peça for diferente da coluna 0 e estiver vazia ou só restar 1 movimento
                            # Ou se a peça estiver nas colunas á beira da casa vencedora
                            if op != 1 and row - 1 != 0 and (state.get_grid()[row - 1][col] == -1 or moves == 1) or row - 1 == 0 and 2 <= col <= 3:
                                print("4 - Para cima")
                                can_move = True
                                ative4 = True

                        if can_move:  # Se for possivel mover a peça

                            print("\nNº de movimentos restantes: " + str(moves))
                            op = int(input("Quer mover esta peça para onde: "))

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
                                ative1 = False

                            elif op == 2 and ative2:  # Se a opção escolhida for 2 e esta opção estiver disponivel
                                col -= 1
                                # Se calhar na casa de outra peça fica com os movimentos dessa peça
                                if state.get_grid()[row][col] != -1:
                                    moves += state.get_grid()[row][col]
                                # A nova posição fica com o valor da peça e a anterior fica vazia
                                state.get_grid()[row][col] = state.get_grid()[row][col + 1]
                                state.get_grid()[row][col + 1] = state.EMPTY_CELL
                                ative2 = False

                            elif op == 3 and ative3:  # Se a opção escolhida for 3 e esta opção estiver disponivel
                                col += 1
                                # Se calhar na casa de outra peça fica com os movimentos dessa peça
                                if state.get_grid()[row][col] != -1:
                                    moves += state.get_grid()[row][col]
                                # A nova posição fica com o valor da peça e a anterior fica vazia
                                state.get_grid()[row][col] = state.get_grid()[row][col - 1]
                                state.get_grid()[row][col - 1] = state.EMPTY_CELL
                                ative3 = False

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
                                ative4 = False

                            else:  # Se for selecionada uma opção que não seja possivel
                                moves += 1
                                print(color.RED + "That movement is not possible!" + color.END)

                            moves -= 1

                            if moves != 0:
                                state.display()

                        else:  # Se a peça não possa ser movida

                            print(color.RED + "You can´t move that piece!\n" + color.END)
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
                        print(color.YELLOW + f"Player {state.get_acting_player()}:" + color.END)
                        return GygesAction(1, int(input("\nChoose the column where you want to put this piece: ")))

                    else:

                        # O jogador 1 irá ficar com a parte de baixo do tabuleiro
                        print(color.YELLOW + f"Player {state.get_acting_player()}:" + color.END)
                        return GygesAction(6, int(input("\nChoose the column where you want to put this piece: ")))

            except Exception:
                continue

    def event_action(self, pos: int, action, new_state: GygesState):
        # ignore
        pass

    def event_end_game(self, final_state: GygesState):
        # ignore
        pass
