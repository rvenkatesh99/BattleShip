import sys
from BattleShip.game import Game

if __name__ == '__main__':
    board_dim = 10
    for i in range(len(sys.argv)):
        print(i, sys.argv[i])
    with open(sys.argv) as infile:
        for line in infile:

    if len(sys.argv) >= 2:
        board_dim = int(sys.argv[1])

    game = Game(board_dim)
    game.play()