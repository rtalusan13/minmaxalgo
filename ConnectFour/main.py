from ConnectFour.ConnectFourBoard import ConnectFourBoard
from ConnectFour.ConnectFourHumanPlayer import ConnectFourHumanPlayer
from ConnectFour.ConnectFourLUNARPlayer import ConnectFourLUNARPlayer
from GameEngine import GameEngine
from RandomPlayer import RandomPlayer

player1 = ConnectFourHumanPlayer()
player2 = ConnectFourLUNARPlayer()
#player2 = RandomPlayer()

board = ConnectFourBoard([player1, player2])

engine = GameEngine(board)

winner = engine.run(True)

if winner == player1 :
    print("The winner is player 1!")
else:
    print("The winner is player 2!")
