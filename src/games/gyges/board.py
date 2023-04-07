
from src.games.gyges.piece import Piece


class Board:

    #construtor importante para criação da classe
    def __init__(self):
        self.board = [[None]* 8 for _ in range(8) ] # vai percorrer uma matriz de 8 (para ter mais espaço) #None é existencia de nada mas é so para ter uma coisa lá  # aqui ja se cria o tabuleiro vazio
        self.init_board()  # vai a posicao do board e mete uma peca la

    def get_piece(self):
        return self.piece

    def init_board(self):
        self.place_piece(Piece("L1"), 1, 0)
        self.place_piece(Piece("L3"), 2, 0)
        self.place_piece(Piece("L2"), 3, 0)
        self.place_piece(Piece("L2"), 4, 0)
        self.place_piece(Piece("L3"), 5, 0)
        self.place_piece(Piece("L1"), 6, 0)
        self.place_piece(Piece("L2"), 1, 7)
        self.place_piece(Piece("L1"), 2, 7)
        self.place_piece(Piece("L2"), 3, 7)
        self.place_piece(Piece("L3"), 4, 7)
        self.place_piece(Piece("L3"), 5, 7)
        self.place_piece(Piece("L1"), 6, 7)


    def place_piece(self, piece, row, col):
         self.board[row][col] = piece

    def print_board(self):
        for row in self.board:
            for piece in row:
                if piece is None:
                    print("-", end=" ")
                else:
                    print(piece.get_piece_type(), end=" ")
            print()


