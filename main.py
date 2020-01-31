import sys
from game import Game
from ship import Ship

if __name__ == '__main__':
    with open(sys.argv[1]) as infile:
        content = infile.readlines()

    temp_str = content[0]
    type(temp_str)
    temp_str = temp_str.strip()
    num_row, num_col = temp_str.split(" ")
    num_row = int(num_row)
    num_col = int(num_col)

    ship_list = []
    for i in range(1, len(content)):
        temp_str = content[i]
        temp_str = temp_str.strip()
        ship_name, length = temp_str.split(" ")
        new_ship = Ship(ship_name, length)
        ship_list.append(new_ship)

    # if len(sys.argv) >= 2:
    #     board_dim = int(sys.argv[1])

    print(Game(num_row, num_col))

    game = Game(num_row,num_col)

    game.play()