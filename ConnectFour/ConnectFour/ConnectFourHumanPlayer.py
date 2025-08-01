from Player import Player
from ConnectFour.ConnectFourMove import ConnectFourMove

class ConnectFourHumanPlayer(Player):
    def __init__(self):
        super().__init__()

    def getMove(self, board):
        valid_moves = board.getPossibleMoves()
        print('\nMoves:', [valid.column + 1 for (i, valid) in enumerate(valid_moves) if valid])

        while True:
            move = ConnectFourMove(self, int(input()) - 1)
            if move in valid_moves:
                break
            else:
                print('Invalid move')
        return move