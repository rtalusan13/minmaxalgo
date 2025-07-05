from Player import Player
from Quoridor.QuoridorMove import QuoridorMove
from random import Random

class QuoridorLUNARPlayer(Player):
    def __init__(self):
        super().__init__() 

    def getMove(self, board):
        
        # Here is where your code goes


                
        old_coord = board.players[4].coord
        old_coord.y += 1
        return QuoridorMove.move_pawn(old_coord, self)