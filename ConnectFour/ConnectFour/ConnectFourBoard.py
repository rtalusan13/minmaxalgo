import GameState
from ConnectFour.ConnectFourMove import ConnectFourMove

import pygame
pygame.init()

BLACK = 0,0,0
RED = 255,0,0
BLUE = 0,0,255
WHITE = 255, 255, 255

NCOLUMNS = 7
NROWS = 6

pygame.font.init()

class ConnectFourBoard(GameState.GameState):
    
    def __init__(self, players):
        super().__init__(players)
        if len(players) != 2:
            raise ValueError("Connect Four must have two players.")
        self.columns = []
        for enum in range(NCOLUMNS):
            self.columns.append([])
        self.internalCurrentPlayer = players[0]
        
    def clone(self):
        newBoard = ConnectFourBoard(self.players)
        newBoard.columns = [list(column) for column in self.columns]
        newBoard.internalCurrentPlayer = self.internalCurrentPlayer
        return newBoard
    
    def getPossibleMoves(self):       
        possibleMoves = []
        for enum in range(NCOLUMNS):
            if len(self.columns[enum]) < NROWS:
                possibleMoves.append(ConnectFourMove(self.internalCurrentPlayer, enum))
        return possibleMoves
    
    def checkIsValid(self, move):
        if move.column < 0 or move.column > NCOLUMNS - 1:
            return False
        if len(self.columns[move.column]) >= NROWS:
            return False
        return True

    def doMove(self, move):
        self.columns[move.column].append(move.player)
        self.internalCurrentPlayer = self.nextPlayer()
        return self
    
    def currentPlayer(self):
        return self.internalCurrentPlayer
    
    def nextPlayer(self):
        if self.internalCurrentPlayer == self.players[0]:
            return self.players[1]
        else:
            return self.players[0]
        
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
        if column < 0 or column > NCOLUMNS - 1 or row < 0 or row > NROWS - 1 or len(self.columns[column]) <= row:
            return False
        else:
            return True
        
    def initializeDrawing(self):
        self.rows = NROWS
        self.cols = NCOLUMNS
        self.screen = pygame.display.set_mode((640, 480))

        self.width = 640
        self.height = 480
        self.radius = 480 / 20
        self.box_size = 480 / (self.rows + 2)
        self.left_disp_offset = self.box_size * 2
        self.top_disp_offset = self.box_size

        self.game_closed = False     
        
    def drawBoard(self):
        if not self.game_closed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_closed = True
                    pygame.quit()

            # Reset screen
            self.screen.fill(BLACK)

            # Drawing the grid
            my_font = pygame.font.SysFont("monospace", 20)
            for row_num in range(self.rows + 1):
                row_start = (self.left_disp_offset, self.top_disp_offset + (self.box_size * row_num))
                row_end = (self.left_disp_offset + (self.box_size * self.cols), self.top_disp_offset + (self.box_size * row_num))
                pygame.draw.line(self.screen, WHITE, row_start, row_end)
            for col_num in range(self.cols + 1):
                col_start = (self.left_disp_offset + (self.box_size * col_num), self.top_disp_offset)
                col_end = (self.left_disp_offset + (self.box_size * col_num), self.top_disp_offset + (self.box_size * self.rows))
                if col_num > 0:
                    col_label = my_font.render(str(col_num), 1, WHITE)
                    self.screen.blit(col_label, (self.left_disp_offset + (self.box_size * col_num) - self.box_size / 2, self.height - 40))
                pygame.draw.line(self.screen, WHITE, col_start, col_end)

            # Drawing pieces
            for col_num, col in enumerate(self.columns):
                for row_num, element in enumerate(col):
                    pos = (int(self.box_size * (col_num + 0.5)) + self.left_disp_offset,
                           int(self.box_size * ((NROWS - row_num - 1) + 0.5)) + self.top_disp_offset)
                    if element == self.players[0]:
                        color = RED
                    else:
                        color = BLUE

                    pygame.draw.circle(self.screen, color, pos, self.radius)
            pygame.display.flip()
            #pygame.time.wait(1000)
        

