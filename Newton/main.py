from random import Random
from re import I
from GameEngine import GameEngine
from Newton.NewtonBoard import NewtonBoard
from Newton.NewtonHumanPlayer import NewtonHumanPlayer
from Newton.NewtonLUNARPlayer import NewtonLUNARPlayer
from RandomPlayer import RandomPlayer
from TiePlayer import TiePlayer
from MinimaxPlayer import MinimaxPlayer

#player1 = ConnectFourHumanPlayer()
#player1 = ConnectFourYOURNAMEPlayer()
#player2 = RandomPlayer()
#player2 = ConnectFourDrDongPlayer()
#player2 = ConnectFourLUNARPlayer()

player1 = NewtonHumanPlayer()
#player2 = RandomPlayer()
player2 = NewtonLUNARPlayer()

board = NewtonBoard([player1, player2])

engine = GameEngine(board)

winner = engine.run(True)

if winner == player1:
    print("The winner is player 1!")
elif winner == player2:
    print("The winner is player 2!")
elif isinstance(winner, TiePlayer):
    print("The game was a tie!")
else:
    print("I don't even know what you did to get here!")
