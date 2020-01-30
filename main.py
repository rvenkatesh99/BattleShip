import sys
from BattleShip.game import Game

if __name__ == '__main__':
    board_dim = 10
    for i in range(len(sys.argv)):
        print(i, sys.argv[i])

    with open(sys.argv[1]) as infile:
        content = infile.readlines()

    temp_str = content[0]
    type(temp_str)
    temp_str = temp_str.strip()
    nr, nc = temp_str.split(" ")
    nr = int(nr)
    nc = int(nc)

    boat_dict = {}
    for i in range(1,len(content)):
        temp_str = content[i]
        temp_str = temp_str.strip()
        boat, length = temp_str.split(" ")
        boat_dict[boat] = int(length)
        print(boat_dict)


    # if len(sys.argv) >= 2:
    #     board_dim = int(sys.argv[1])

    game = Game(nr,nc)
    game.play()