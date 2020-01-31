import ship


class MoveError(Exception):
    pass


class Move(object):
    def __init__(self, maker: "Player", ship: "Ship", row: int, col: int) -> None:
        self.maker = maker
        self.row = row
        self.col = col

    @classmethod
    def from_string(cls, maker: "Player", str_move: str) -> "Move":
        """
        :param maker:
        :param str_move: should be in format row, col
        :return:
        """
        try:
            row, col = str_move.split(',')
        except ValueError:
            raise MoveError(f'{str_move} is not in the form row,col')

        try:
            row = int(row)
        except ValueError:
            raise MoveError(f'{row} needs to be an integer. {row} is not an integer')

        try:
            col = int(col)
        except ValueError:
            raise MoveError(f'{col} needs to be an integer. {col} is not an integer')

        return cls(maker, row, col)

    def make(self, the_board: "Board"):
        if not the_board.is_in_bounds(self.row, self.col):
            raise MoveError(f'{self.row},{self.col} is not in bounds')

        elif the_board[self.row, self.col] != the_board.blank_char:
            raise MoveError(f' You cannot play at {self.row},{self.col} because someone already played there')

        else:
            the_board[self.row][self.col] = self.maker.piece

    def place_ship_horiz(self, player_board: "Board"):
        if not player_board.is_in_bounds(self.row, self.col):
            raise MoveError(f'{self.row},{self.col} is not in bounds')

        elif player_board[self.row, self.col] != player_board.blank_char:
            raise MoveError(
                f' You cannot place your ship at {self.row},{self.col} because you already placed a ship there')

        else:
            for i in range(ship.Ship.length):
                player_board[self.row + i][self.col] = self.ship.char

   def place_ship_vert(self, player_board: "Board"):
        if not player_board.is_in_bounds(self.row, self.col):
            raise MoveError(f'{self.row},{self.col} is not in bounds')

        elif player_board[self.row, self.col] != player_board.blank_char:
            raise MoveError(
                f' You cannot place your ship at {self.row},{self.col} because you already placed a ship there')

        else:
            for i in range(ship.Ship.length):
                player_board[self.row][self.col + i] = self.ship.char
