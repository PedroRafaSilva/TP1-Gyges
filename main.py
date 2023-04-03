from src.games.game_simulator import GameSimulator

from src.games.gyges.players.human import HumanGygesPlayer
from src.games.gyges.players.greedy import GreedyGygesPlayer
from src.games.gyges.players.minimax import MinimaxGygesPlayer
from src.games.gyges.players.Random import RandomGygesPlayer
from src.games.gyges.simulator import GygesSimulator

def run_simulation(desc: str, simulator: GameSimulator, iterations: int):
    print(f"----- {desc} -----")

    for i in range(0, iterations):
        simulator.change_player_positions()
        simulator.run_simulation()

    print("Results for the game:")
    simulator.print_stats()


def main():
    print("ESTG IA Games Simulator")

    num_iterations = 10

    tictactoe_simulations = [
         # uncomment to play as human
        {
           "name": "TicTacToe - Human VS Random",
            "player1": HumanGygesPlayer("Human"),
            "player2": HumanGygesPlayer("Random")
        },
        """"{
            "name": "TicTacToe - Random VS Random",
            "player1": RandomGygesPlayer("Random 1"),
            "player2": RandomGygesPlayer("Random 2")
        },
        {
            "name": "TicTacToe - Greedy VS Random",
            "player1": GreedyGygesPlayer("Greedy"),
            "player2": RandomGygesPlayer("Random")
        },
        {
            "name": "TicTacToe - Minimax VS Random",
            "player1": MinimaxGygesPlayer("Minimax"),
            "player2": RandomGygesPlayer("Random")
        },
        {
            "name": "TicTacToe - Minimax VS Greedy",
            "player1": MinimaxGygesPlayer("Minimax"),
            "player2": GreedyGygesPlayer("Greedy")
        }"""]

    for sim in tictactoe_simulations:
        run_simulation(sim["name"], GygesSimulator(sim["player1"], sim["player2"]), num_iterations)

if __name__ == "__main__":
    main()
