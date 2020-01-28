import sys

if __name__ == '__main__':
    board_dim = 3
    if len(sys.argv) >= 2:
        board_dim = int(sys.argv[1])

    game = BattleshipGame(board_dim)
    game.play()