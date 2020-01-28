from typing import Iterable, TypeVar
from .board import Board
from .player import Player
from .ship import Ship

T = TypeVar('T')
# Class for game play
class BattleshipGame(object):
    def __init__(self, dimensions: int, blank_char: str = '*') -> None:
        self.blank_char = blank_char
        self.board = Board(dimensions, dimensions, blank_char)
        self.players = [Player() for _ in range(2)]
        self.player_ships = [Ship() for _ in range()]
        self.curr_player_turn = 0

    def play(self) -> None:
        while not self.is_game_over():
            self.display_game_state()
            curr_player = self.get_curr_player()
            curr_player.take_turn()
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
        # if self.curr_player_turn == 0
        # self.curr_Player_turn = 1
        # else:
        # self._cur_player_turn = 1

    def get_cur_player(self) -> "Player":
        return self.players[self._curr_player_turn]