from Move import Move

class NewtonMove(Move):
    
    """
    A move in Newton, which includes the player who made the move and the column in which the move was made, as well as whether it was a drop or a flip
    """
    
    def __init__(self, player, column, flip):
        super().__init__()
        self.player = player
        self.column = column
        self.flip = flip
    
    def __eq__(self, other):
        return (isinstance(other, NewtonMove) and (self.player == other.player) and (self.column == other.column) and (self.flip == other.flip))
    