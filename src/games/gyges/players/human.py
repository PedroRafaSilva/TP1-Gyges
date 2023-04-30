from src.games.gyges.action import GygesAction
from src.games.gyges.player import GygesPlayer
from src.games.gyges.state import GygesState, Color


class HumanGygesPlayer(GygesPlayer):

    def __init__(self, name):
        super().__init__(name)

    def game_rules(self):
        option = 0
        while option != 1:
            print("-------------------------Regras do jogo-----------------------")
            print("- O tabuleiro inicia vazio.")
            print("- Existem 2 jogadores.")
            print("- Cada jogador tem 6 peças de cada nível "
                  "(2 peças de 3 níveis, 2 peças de 2 níveis e 2 peças de 1 nível).")
            print("- Cada jogador só pode movimentar a peça mais próxima de si.")
            print("- As peças só podem ser movimentadas na vertical e na horizontal.")
            print("- Não há movimentos diagonais neste jogo.")
            print("- As peças devem obrigatoriamente, percorrer o número de casas correspondente ao seu nível.")
            print("- As peças podem transitar sobre outras peças.")
            print("- As peças não podem saltar casas.")
            print("- Não se pode passar duas vezes pela mesma casa.")
            print("- As peças podem encerrar a sua jogada sobre outra peça onde podem adquirir a quantidade de "
                  "movimentos da peça em que está abaixo e continuar o movimento.")
            print("- As casas da vitória só podem ser alcançadas pelas 2 casas que fazem vizinhança com esta, assim,\n "
                  "a casa da vitória do jogador 1, só pode ser alcançada a partir das casas (0,2) e (0,3) e a casa da\n"
                  "vitória do jogador 2, só pode ser alcançada a partir das casas (7,2) e (7,3).")
            print("- O jogo termina quando um jogador não consegue encontrar nenhuma maneira de impedir a vitória "
                  "do seu adversário.")
            print("\nContinuar?")
            print("1 - Sim   0 - Não")
            option = int(input("Opção: "))

    def get_action(self, state: GygesState):
        if state.get_turn() == 1:
            self.game_rules()
        print("\n")
        state.display()
        while True:
            # noinspection PyBroadException
            try:

                op = row = col = 0
                proceed = False
                ative1 = ative2 = ative3 = ative4 = False

                if state.get_turn() > 12:  # Se as peças estiverem todas colocadas

                    while not proceed:  # Enqaunto não for escolhida a(s) peça(s) mais próxima(s)

                        print("\nInsert the positions of a piece, " + Color.YELLOW +
                              f"Player {state.get_acting_player()}" + Color.END)

                        row = int(input("Choose the row of the piece: "))
                        col = int(input("Choose the column of the piece: "))

                        # Se o jogador 0 escolher o campo com uma peça mais próxima dele, continua
                        if state.get_acting_player() == 0 and row == state.get_closest_playable_row() \
                                and state.get_grid()[row][col] != -1:

                            proceed = True

                        # Se o jogador 1 escolher o campo com uma peça mais próxima dele, continua
                        elif state.get_acting_player() == 1 and row == state.get_closest_playable_row() \
                                and state.get_grid()[row][col] != -1:

                            proceed = True

                        # Caso contrário volta a escolher a linha e a coluna da peça a jogar
                        else:

                            proceed = False
                            print(Color.RED + f"Choose a piece that is in the row number: "
                                              f"{state.get_closest_playable_row()}!!!" + Color.END)
                            state.display()

                    old_pos = [row, col]  # Posição anterior da peça
                    moves = state.get_grid()[row][col]  # O número de movimentos é igual ao tipo de peça escolhido

                    while moves != 0:  # Enquanto houver movimentos

                        can_move = False
                        print("\nMovements")

                        if state.get_acting_player() == 0:  # Apenas o jogador 0 pode mover a peça para baixo
                            """
                            Se a linha abaixo da peça for diferente da coluna 7 e estiver vazia ou só restar 1 movimento
                            Ou se a peça estiver nas colunas á beira da casa vencedora
                            """
                            if row + 1 != 7 and (state.get_grid()[row + 1][col] == -1 or moves == 1) or \
                                    (row + 1 == 7 and 2 <= col <= 3 and moves == 1):

                                print("1 - Down")
                                ative1 = True
                                can_move = True

                        """
                        Se o ultimo movimento não foi para a direita e a coluna da esquerda estiver vazia
                        e diferente de 0 ou a coluna da esquerda estiver ocupada mas for o ultimo movimento da peça
                        """
                        if op != 3 and col != 0 and (state.get_grid()[row][col - 1] == -1 or moves == 1):
                            print("2 - Left")

                            can_move = True
                            ative2 = True

                        """
                        Se o ultimo movimento não foi para a esquerda e a coluna da esquerda estiver vazia
                        e diferente de 5 ou a coluna da direita estiver ocupada mas for o ultimo movimento da peça
                        """
                        if op != 2 and col != 5 and (state.get_grid()[row][col + 1] == -1 or moves == 1):

                            print("3 - Right")
                            can_move = True
                            ative3 = True

                        if state.get_acting_player() == 1:  # Apenas o jogador 1 pode mover a peça para cima
                            """
                            Se a linha acima da peça for diferente da coluna 0 e estiver vazia ou só restar 1 movimento
                            Ou se a peça estiver nas colunas á beira da casa vencedora
                            """
                            if op != 1 and row - 1 != 0 and (state.get_grid()[row - 1][col] == -1 or moves == 1) or \
                                    (row - 1 == 0 and 2 <= col <= 3 and moves == 1):

                                print("4 - Up")
                                can_move = True
                                ative4 = True

                        if can_move:  # Se for possivel mover a peça

                            print("\nNº of movements left: " + str(moves))
                            op = int(input("Where do you want to move this piece?: "))

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
                                print(Color.RED + "That movement is not possible!" + Color.END)

                            moves -= 1
                            ative1 = ative2 = ative3 = ative4 = False

                            if moves != 0:
                                state.display()

                        else:  # Se a peça não possa ser movida

                            print(Color.RED + "You can´t move that piece, becaus it is blocked!\n" + Color.END)
                            print(Color.RED + "Please, try again!\n" + Color.END)

                            # São colocados estes valores para que o validate_action retorne false
                            # E o jogador tenha outra hípotese
                            row = -1
                            col = -1
                            moves = 0

                    new_pos = [row, col]  # A nova posição da peça
                    return GygesAction(old_pos, new_pos)

                else:

                    # O jogador 0 irá ficar com a parte de cima do tabuleiro
                    if state.get_acting_player() == 0:

                        print(Color.YELLOW + f"Player {state.get_acting_player()}:" + Color.END)
                        return GygesAction(1, int(input("\nChoose the column where you want to put this piece: ")))

                    else:

                        # O jogador 1 irá ficar com a parte de baixo do tabuleiro
                        print(Color.YELLOW + f"Player {state.get_acting_player()}:" + Color.END)
                        return GygesAction(6, int(input("\nChoose the column where you want to put this piece: ")))

            except Exception:
                continue

    def event_action(self, pos: int, action, new_state: GygesState):
        # ignore
        pass

    def event_end_game(self, final_state: GygesState):
        # ignore
        pass
