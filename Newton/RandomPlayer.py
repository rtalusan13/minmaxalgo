import Player
import random

class RandomPlayer(Player.Player):
    def __init__(self):
        super().__init__()

    def getMove(self, board):
        valids = board.getPossibleMoves()
        return random.choice(valids)