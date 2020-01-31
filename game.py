from typing import TypeVar

import board
import player
import ship
from move import Move, MoveError

T = TypeVar('T')


# Class for game play - takes in user input to initialize both player boards, list of ships
class Game(object):
    def __init__(self, dimension_row: int, dimension_col: int, ship_list: list, blank_char: str = '*') -> None:
        self.ship_list = ship_list
        self.blank_char = blank_char
        self.board = board.Board(dimension_row, dimension_col, blank_char)

        self.players = []
        for player_num in range(2):
            self.players.append(player.Player(self.players, self.board, self.ship_list))

        self._curr_player_turn = 0

    def play(self) -> None:
        while not self.is_game_over():
            self.display_game_state()
            curr_player = self.get_curr_player()
            #curr_player.take_turn(self.board)
            self.update_board()
            self.change_turn()
        self.display_winner()

    def display_game_state(self) -> None:
        self.players[self._curr_player_turn % 1].player_board.print_scan_board()
        self.players[self._curr_player_turn].player_board.print_board()

    def is_game_over(self) -> None:
        return self.someone_won()

    def someone_won(self) -> bool:
        # How does someone win in battleship? All the opponent ships are destroyed
        for i in range(2):
            if self.players[i].player_board.are_ships_destroyed():
                return True
        return False

    def change_turn(self) -> None:
        self._curr_player_turn = (self._curr_player_turn + 1) % 2
        # if self._curr_player_turn == 0:
        # self._curr_player_turn = 1
        # else:
        # self._curr_player_turn = 1

    def get_curr_player(self) -> "Player":
        return self.players[self._curr_player_turn]

    def convert_hit_from_str(self) -> "Move":
        str_hit = input(f'{self.curr_player} enter the location you want to fire at in the form row, column: ')
        return Move.from_string(self, self.convert_hit_from_str)

    def do_hit(self, player_board: "Player") -> None:
        while True:
            try:
                move = self.convert_hit_from_str()
                move.make(player_board)
            except MoveError:
                print(MoveError)

    def update_board(self) -> None:
        self.players[self._curr_player_turn % 1].player_board.do_hit(self.player_board) #add hit will be a board function

