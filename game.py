from typing import TypeVar

import board
import player

T = TypeVar('T')


# Class for game play
class Game(object):
    def __init__(self, dimension_row: int, dimension_col: int, blank_char: str = '*') -> None:
        self.blank_char = blank_char
        self.board = board.Board(dimension_row, dimension_col, blank_char)

        self.players = []
        for player_num in range(2):
            self.players.append(player.Player(self.players, blank_char))

        self._curr_player_turn = 0

    def play(self) -> None:
        while not self.is_game_over():
            self.display_game_state()
            curr_player = self.get_curr_player()
            curr_player.place_ships(self.board)
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