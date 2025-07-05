from random import Random

from GameEngine import GameEngine
from RandomPlayer import RandomPlayer
from TiePlayer import TiePlayer
from MinimaxPlayer import MinimaxPlayer
# from Newton.NewtonBoard import NewtonBoard
# from Newton.NewtonHumanPlayer import NewtonHumanPlayer
# from Newton.NewtonYOURNAMEPlayer import NewtonYOURNAMEPlayer

# player1 = NewtonHumanPlayer()
# player2 = NewtonYOURNAMEPlayer()
# #player2 = RandomPlayer()

# board = NewtonBoard([player1, player2])

from Quoridor.QuoridorBoard import QuoridorBoard
from Quoridor.QuoridorHumanPlayer import QuoridorHumanPlayer
from Quoridor.QuoridorLUNARPlayer import QuoridorLUNARPlayer

player1 = QuoridorHumanPlayer()
player2 = QuoridorHumanPlayer()
#player2 = RandomPlayer()

board = QuoridorBoard([player1, player2])

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
