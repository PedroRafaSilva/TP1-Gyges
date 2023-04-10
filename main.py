from src.games.game_simulator import GameSimulator

from src.games.gyges.players.human import HumanGygesPlayer
from src.games.gyges.players.greedy import GreedyGygesPlayer
from src.games.gyges.players.minimax import MinimaxGygesPlayer
from src.games.gyges.players.Random import RandomGygesPlayer
from src.games.gyges.simulator import GygesSimulator


def run_simulation(desc: str, simulator: GameSimulator, iterations: int):
    print(f"----- {desc} -----")

    for i in range(0, iterations):
        # simulator.change_player_positions()
        simulator.run_simulation()
    print("Results for the game:")
    simulator.print_stats()


def main():
    print("ESTG IA Games Simulator")

    num_iterations = 4

    gyges_simulations = [
         # uncomment to play as human
        #{
        #   "name": "Gyges - Human VS Human",
        #    "player1": HumanGygesPlayer("Human 1"),
        #    "player2": HumanGygesPlayer("Human 2")
        #},
        #{
        #    "name": "Gyges - Human VS Random",
        #    "player1": HumanGygesPlayer("Human 1"),
        #    "player2": RandomGygesPlayer("Random")
        #},
        {
            "name": "Gyges - Random VS Random",
            "player1": RandomGygesPlayer("Random 1"),
            "player2": RandomGygesPlayer("Random 2")
        }
    ]

    for sim in gyges_simulations:

        run_simulation(sim["name"], GygesSimulator(sim["player1"], sim["player2"]), num_iterations)


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

