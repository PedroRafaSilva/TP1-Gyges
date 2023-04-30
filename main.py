from games.gyges.state import Color
from src.games.game_simulator import GameSimulator
from src.games.gyges.players.human import HumanGygesPlayer
from src.games.gyges.players.greedy import GreedyGygesPlayer
from src.games.gyges.players.minimax import MinimaxGygesPlayer
from src.games.gyges.players.Random import RandomGygesPlayer
from src.games.gyges.simulator import GygesSimulator


def run_simulation(desc: str, simulator: GameSimulator, iterations: int):
    print(Color.GREEN + f"\n----- {desc} -----" + Color.END)

    for i in range(0, iterations):
        # simulator.change_player_positions()
        simulator.run_simulation()
    print(Color.GREEN + "Results for the game:" + Color.END)
    simulator.print_stats()


def print_main_menu():
    print('\n-------------------------------------')
    print('--- Gyges Game                    ---')
    print('-------------------------------------')
    print('--- 1 - Humano vs Humano          ---')
    print('--- 2 - Humano vs AI              ---')
    print('--- 3 - AI vs AI                  ---')
    print('-------------------------------------')
    print('--- 0 - Sair                      ---')
    print('-------------------------------------')


def print_ai_menu():
    print('\n-------------------------------------')
    print('--- Seleção da IA                 ---')
    print('-------------------------------------')
    print('--- 1 - Random                    ---')
    print('--- 2 - Greedy                    ---')
    print('--- 3 - Minimax                   ---')
    print('-------------------------------------')
    print('--- 4 - Voltar Atrás              ---')
    print('--- 0 - Sair                      ---')
    print('-------------------------------------')


def main():
    opc = 1
    gyges_simulations = []
    num_iterations = 0

    while opc != 0:
        print("\n\nESTG IA Games Simulator")

        print_main_menu()

        print('Escolha uma opção: ', end='')
        opc = int(input())

        if opc == 1:
            num_iterations = int(input("\nNº de interações: "))
            gyges_simulations = [
                {
                    "name": "Gyges - Human VS Human",
                    "player1": HumanGygesPlayer("Human 1"),
                    "player2": HumanGygesPlayer("Human 2")
                }
            ]

        if opc == 2:

            print_ai_menu()

            print('Escolha uma opção: ', end='')
            opc2 = int(input())

            if opc2 == 1:
                num_iterations = int(input("\nNº de interações: "))
                gyges_simulations = [
                    {
                        "name": "Gyges - Human VS Random",
                        "player1": HumanGygesPlayer("Human 1"),
                        "player2": RandomGygesPlayer("Random 1")
                    }
                ]

            elif opc2 == 2:
                num_iterations = int(input("\nNº de interações: "))
                gyges_simulations = [
                    {
                        "name": "Gyges - Human VS Greedy",
                        "player1": HumanGygesPlayer("Human 1"),
                        "player2": GreedyGygesPlayer("Greedy 1")
                    }
                ]

            elif opc2 == 3:
                num_iterations = int(input("\nNº de interações: "))
                gyges_simulations = [
                    {
                        "name": "Gyges - Human VS Minimax",
                        "player1": HumanGygesPlayer("Human 1"),
                        "player2": MinimaxGygesPlayer("Minimax 1")
                    }
                ]

            elif opc2 == 4:
                print()

        if opc == 3:

            print_ai_menu()

            print('Escolha uma opção: ', end='')
            opc = int(input())

            if opc == 1:

                print("\nRandom")
                print_ai_menu()

                print('Escolha uma opção: ', end='')
                opc = int(input())

                if opc == 1:
                    num_iterations = int(input("\nNº de interações: "))
                    gyges_simulations = [
                        {
                            "name": "Gyges - Random VS Random",
                            "player1": RandomGygesPlayer("Random 1"),
                            "player2": RandomGygesPlayer("Random 2")
                        }
                    ]

                elif opc == 2:
                    num_iterations = int(input("\nNº de interações: "))
                    gyges_simulations = [
                        {
                            "name": "Gyges - Random VS Greedy",
                            "player1": RandomGygesPlayer("Random 1"),
                            "player2": GreedyGygesPlayer("Greedy 1")
                        }
                    ]

                elif opc == 3:
                    num_iterations = int(input("\nNº de interações: "))
                    gyges_simulations = [
                        {
                            "name": "Gyges - Random VS Minimax",
                            "player1": RandomGygesPlayer("Random 1"),
                            "player2": MinimaxGygesPlayer("Minimax 1")
                        }
                    ]

                elif opc == 4:
                    print()

            elif opc == 2:
                print("\nGreedy")
                print_ai_menu()

                print('Escolha uma opção: ', end='')
                opc = int(input())

                if opc == 1:
                    num_iterations = int(input("\nNº de interações: "))
                    gyges_simulations = [
                        {
                            "name": "Gyges - Greedy VS Random",
                            "player1": GreedyGygesPlayer("Greedy 1"),
                            "player2": RandomGygesPlayer("Random 1")
                        }
                    ]

                elif opc == 2:
                    num_iterations = int(input("\nNº de interações: "))
                    gyges_simulations = [
                        {
                            "name": "Gyges - Greedy VS Greedy",
                            "player1": GreedyGygesPlayer("Greedy 1"),
                            "player2": GreedyGygesPlayer("Greedy 2")
                        }
                    ]

                elif opc == 3:
                    num_iterations = int(input("\nNº de interações: "))
                    gyges_simulations = [
                        {
                            "name": "Gyges - Greedy VS Minimax",
                            "player1": GreedyGygesPlayer("Greedy 1"),
                            "player2": MinimaxGygesPlayer("Minimax 1")
                        }
                    ]

                elif opc == 4:
                    print()

            elif opc == 3:

                print("\nMinimax")
                print_ai_menu()

                print('Escolha uma opção: ', end='')
                opc = int(input())

                if opc == 1:
                    num_iterations = int(input("\nNº de interações: "))
                    gyges_simulations = [
                        {
                            "name": "Gyges - Minimax VS Random",
                            "player1": MinimaxGygesPlayer("Minimax 1"),
                            "player2": RandomGygesPlayer("Random 1")
                        }
                    ]

                elif opc == 2:
                    num_iterations = int(input("\nNº de interações: "))
                    gyges_simulations = [
                        {
                            "name": "Gyges - Minimax VS Greedy",
                            "player1": MinimaxGygesPlayer("Minimax 1"),
                            "player2": GreedyGygesPlayer("Greedy 1")
                        }
                    ]

                elif opc == 3:
                    num_iterations = int(input("\nNº de interações: "))
                    gyges_simulations = [
                        {
                            "name": "Gyges - Minimax VS Minimax",
                            "player1": MinimaxGygesPlayer("Minimax 1"),
                            "player2": MinimaxGygesPlayer("Minimax 2")
                        }
                    ]

                elif opc == 4:
                    print()

            elif opc == 4:
                print()

            elif opc == 0:
                print("\n\nAdeus!!")

        if opc != 0 and opc != 4:
            for sim in gyges_simulations:
                run_simulation(sim["name"], GygesSimulator(sim["player1"], sim["player2"]), num_iterations)
                num_iterations = 0


if __name__ == "__main__":
    main()

    """
    As casas vencedoras deverão ser definidas no array como colunas 2 e 3 das linhas 0 e 7 pois como a IA só se move 
    verticalmente e horizontalmente é masi simples fazer as verificações do win state 
    
    EX:
    Jogada linha 2 coluna 2 -> linha 0 coluna 2
    ou
    Jogada linha 2 coluna 3 -> linha 0 coluna 3
    Se fosse no meio seria basicamente coluna 2.5, o que seria mais dificil para calcular
    
    Para mostrar podem na mesma mostrar apenas uma casa, seria só no backend que seria 2 colunas nas linhas de win
    Para as casas que não pode ir, iplementar uma block list ou algo semelhante, que ao geras as moves veerifica contra 
    a block list se pode ou não fazer essa move. Usar algo semelhante para a cena de não se poder mover para as casas 
    antigas
    
          BACKEND
        
     0  1  2  3  4  5 
           x  x       	0
     x  x  x  x  x  x 	1
     x  x  x  x  x  x 	2
     x  x  x  x  x  x 	3
     x  x  x  x  x  x 	4
     x  x  x  x  x  x 	5
     x  x  x  x  x  x 	6
           x  x      	7
           
          FRONTEND
           
     0  1  2  3  4  5 
             x       	0
     x  x  x  x  x  x 	1
     x  x  x  x  x  x 	2
     x  x  x  x  x  x 	3
     x  x  x  x  x  x 	4
     x  x  x  x  x  x 	5
     x  x  x  x  x  x 	6
             x       	7	 
    Para a IA remover os moves obliquos e mudar a cena para verificar o win state
    Tmb a cena de blocked moves
    
    Random não é preciso alterar nada :)
    Para as outras alterar para ficar o mais perto possivel das casas de win (acho, não sei bem as regras)
    
    Alterar a cena para a IA saber quasi sao as pecas dela
    
    """
