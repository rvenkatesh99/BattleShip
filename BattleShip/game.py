from typing import Iterable, TypeVar

from . import board
from . import player
from . import ship

T = TypeVar('T')


# Class for game play
class Game(object):
    def __init__(self, dimensions: int, blank_char: str = '*') -> None:
        self.blank_char = blank_char
        self.board = board.Board(dimensions, dimensions, blank_char)

        self.players = []
        for player_num in range(2):
            self.players.append(player.Player(self.players, blank_char))

        self._curr_player_turn = 0
        self.get_player_ships = None

    # Function to read the configuration file
    def read_config_file(self) -> None:
        config_file = None
        with open("3X4board_one_ship.txt") as file_in:
            lines = []
            for line in file_in:
                dimen = line.split()
                lines.append(dimen)
        self.board = lines[:1]
        return self.board

    def play(self) -> None:
        while not self.is_game_over():
            self.display_game_state()
            curr_player = self.get_curr_player()
            curr_player.take_turn(self.board)
            self.change_turn()
        self.display_winner()

    def display_game_state(self) -> None:
        print(self.board)

    def is_game_over(self) -> None:
        return self.someone_won()

    def someone_won(self) -> bool:
        # How does someone win in battleship? All the opponent ships are destroyed
        return self.player_ships_destroyed()

    def player_ships_destroyed(self) -> bool:
        pass

    def change_turn(self) -> None:
        self._curr_player_turn = (self._curr_player_turn + 1) % 2
        # if self._curr_player_turn == 0:
        # self._curr_player_turn = 1
        # else:
        # self._curr_player_turn = 1

    def get_curr_player(self) -> "Player":
        return self.players[self._curr_player_turn]

    # Create player board and scanning board for each player

    # Assign ships to each player
    def get_player_ships(self, *ships) -> "Ship":
        for ships in range:
            return self.ship[self._get_ship_name]