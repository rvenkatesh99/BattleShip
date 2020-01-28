import sys
from BattleShip.src.battleshipgame import BattleshipGame

if __name__ == '__main__':
    board_dim = 5
    for position, value in enumerate(sys.argv):
        print( f'{position}: {value}')
    if len(sys.argv) >= 2:
        board_dim = int(sys.argv[1])

    game = BattleshipGame(board_dim)
    game.play()