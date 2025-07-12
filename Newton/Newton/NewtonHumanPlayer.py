from Player import Player
from Newton.NewtonMove import NewtonMove

class NewtonHumanPlayer(Player):
    def __init__(self):
        super().__init__()

    def getMove(self, board):
        valid_moves = board.getPossibleMoves()
        print("Enter your next move! (1-5 for drops, 6-10 for flips)")

        while True:
            response = int(input()) - 1
            if response >= 5:
                move = NewtonMove(self, response - 5, flip=True)
            else:
                move = NewtonMove(self, response, flip=False)
            if move in valid_moves:
                break
            else:
                print('Invalid move')
        return move