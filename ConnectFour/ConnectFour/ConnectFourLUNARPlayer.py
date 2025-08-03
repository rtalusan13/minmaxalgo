from Player import Player
from ConnectFour.ConnectFourMove import ConnectFourMove
from ConnectFour.ConnectFourBoard import ConnectFourBoard
import random

class ConnectFourLUNARPlayer(Player):
    """def __init__(self):
        super().__init__()
        
    def checkDirectionThree(self, column, row, deltaX, deltaY):
        for i in range(3):
            irow = row + i * deltaY
            icolumn = column + i * deltaX
            if not self.checkCoord(icolumn, irow):
                return False
            if self.columns[icolumn][irow] != self.columns[column][row]:
                return False
# Checks to see if a win is possible from a given coordinate
    def checkThree(self, column, row):
        for deltaX in range(-1, 2, 1):
            for deltaY in range(-1, 2, 1):
                if deltaX == 0 and deltaY == 0:
                    continue
                if self.checkDirection(column, row, deltaX, deltaY):
                    return True
        return False
    
    def getOppThree(self):
        for column, list in enumerate(self.columns):
            for row, entry in enumerate(list):
                if self.checkWin(column, row):
                    return entry
        return 0

    def getMove(self, board):
        
        #possibleMoves = ConnectFourBoard.getPossibleBoards()
        possibleMoves = []
        for enum in range(7):
            if len(self.columns[enum]) < 6:
                possibleMoves.append(ConnectFourMove(self.internalCurrentPlayer, enum))



        for i in range(len(possibleMoves)):
            possibleBoards = []
            for move in possibleMoves:
                newBoard = self.clone()
                newBoard.doMove(move)
                
                if (board.getGameEnded(newBoard)):
                    return ConnectFourMove(self,move)
                
            pass  
    
        #return ConnectFourMove(self, 3)
    




    def getGameEnded(self):
        for column, list in enumerate(self.columns):
            for row, entry in enumerate(list):
                if self.checkWin(column, row):
                    return entry
        return 0

# Checks to see if a win is possible from a given coordinate
    def checkWin(self, column, row):
        for deltaX in range(-1, 2, 1):
            for deltaY in range(-1, 2, 1):
                if deltaX == 0 and deltaY == 0:
                    continue
                if self.checkDirection(column, row, deltaX, deltaY):
                    return True
        return False
    
# Checks to see if a win is possible in a given direction
    def checkDirection(self, column, row, deltaX, deltaY):
        for i in range(4):
            irow = row + i * deltaY
            icolumn = column + i * deltaX
            if not self.checkCoord(icolumn, irow):
                return False
            if self.columns[icolumn][irow] != self.columns[column][row]:
                return False
        return True

# Checks to see if a coordinate is valid
    def checkCoord(self, column, row):
        if column < 0 or column > 7 - 1 or row < 0 or row > 6 - 1 or len(self.columns[column]) <= row:
            return False
        else:
            return True"""
    def getMove(self, board):
        return ConnectFourMove(self, 1)