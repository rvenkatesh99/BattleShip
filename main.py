import sys
from BattleShip.game import Game
from BattleShip.ship import Ship

if __name__ == '__main__':
    board_dim = 10
    for i in range(len(sys.argv)):
        print(i, sys.argv[i])

    with open(sys.argv[1]) as infile:
        content = infile.readlines()

    temp_str = content[0]
    type(temp_str)
    temp_str = temp_str.strip()
    num_row, num_col = temp_str.split(" ")
    num_row = int(num_row)
    num_col = int(num_col)

    ship_dict = {}
    for i in range(1,len(content)):
        temp_str = content[i]
        temp_str = temp_str.strip()
        ship, length = temp_str.split(" ")
        ship_dict[ship] = int(length)

    all_ships = Ship(ship, length)


    # if len(sys.argv) >= 2:
    #     board_dim = int(sys.argv[1])

    game = Game(num_row,num_col)
    game.play()