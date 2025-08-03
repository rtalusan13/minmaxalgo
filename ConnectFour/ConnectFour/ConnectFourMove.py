import Move

class ConnectFourMove(Move.Move):
    
    """
    A move in Connect Four, which includes the player who made the move and the column in which the move was made.
    """
    
    def __init__(self, player, column):
        super().__init__()
        self.player = player
        self.column = column
    
    def __eq__(self, other):
        return (isinstance(other, ConnectFourMove) and (self.player == other.player) and (self.column == other.column))
    