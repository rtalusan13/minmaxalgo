from asyncio import open_connection
from Player import Player
import random

from TiePlayer import TiePlayer

class MinimaxPlayer(Player):
    def __init__(self, depth):
        super().__init__()
        self.depth = depth

    def getMove(self, board):
        newMove, value = self.maximizeBoard(board, 0, self)
        return newMove
        
# Get maximum value possible on board
# Returns as ordered pair of move and value
    def maximizeBoard(self, board, depth, player):
        ended = board.getGameEnded()
        if ended:
            result = board.scoreBoard()
            return None, result[player]

        if depth >= self.depth:
            return None, self.scoreBoard(board, player)

        options = board.getPossibleBoardsAndMoves()
        bestOptions = []
        bestValue = -100000
        for option in options:
            newMove, value = self.maximizeBoard(option[0], depth + 1, board.currentPlayer())
            if value > bestValue:
                bestOptions = [option]
                bestValue = value
            elif value == bestValue:
                bestOptions.append(option)
        
        bestOptions.sort(key=lambda x: self.scoreBoard(x[0], player))

        return bestOptions[0][1], -bestValue
    
# Assign a score to a board
# By default, just a random number
    def scoreBoard(self, board, player):
        return random.uniform(-1, 1)
        