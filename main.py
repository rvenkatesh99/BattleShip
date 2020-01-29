import sys
from BattleShip.game import Game

if __name__ == '__main__':
    board_dim = 5
    for position, value in enumerate(sys.argv):
        print( f'{position}: {value}')
    if len(sys.argv) >= 2:
        board_dim = int(sys.argv[1])

    game = Game(board_dim)
    game.play()