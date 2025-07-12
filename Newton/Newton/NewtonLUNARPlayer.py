from MinimaxPlayer import MinimaxPlayer
from Newton.NewtonMove import NewtonMove
from random import Random

class NewtonLUNARPlayer(MinimaxPlayer):
    def __init__(self):
        super().__init__(3) # This is how many turns to look ahead

    def scoreBoard(self, board, player):
        # Here is where you implement your heuristic
        # It should be a number between -1 and 1, where higher numbers are better for the current player
        return True
        return Random.range(-1, 1)