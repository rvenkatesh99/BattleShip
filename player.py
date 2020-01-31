import ship
from typing import Iterable
from move import Move, MoveError
from board import Board



# ship list within the player class

class Player(object):
    def __init__(self, other_players: Iterable["Player"], player_board: "Board", blank_character: str = "*") -> None:
        self.name = self.get_name_from_player(other_players)
        self.player_board = player_board

    @staticmethod
    def get_name_from_player(other_players: Iterable["Player"]) -> str:
        already_used_names = set([player.name for player in other_players])
        while True:
            name = input('Please enter your name: ')
            if name not in already_used_names:
                return name
            else:
                print(f'{name} has already been used. Pick another name.')

    def __str__(self) -> str:
        return self.name

    @staticmethod
    def get_ship_orientation(self) -> str:
        while True:
            ship_h_or_v = input(
                f'{self.name} Enter horizontal or vertical for the placement of {ships.name} which is {ship.Ship.length} long').strip()
            ship_h_or_v = ship_h_or_v.lower()
            if str.startswith(ship_h_or_v) == "h":
                return self.get_orientation_horiz()
            elif str.startswith(ship_h_or_v) == "v":
                return self.get_orientation_vert()
            else:
                print(f'{ship_h_or_v} does not represent a valid Orientation')

    def get_orientation_horiz(self) -> "Move":
        str_orientation = input(f'{self} enter the location you want to place {ship.Ship.name} which is {ship.Ship.length} long in the form row, column: ')
        return Move.from_string(self, str_orientation)

    def get_orientation_vert(self) -> "Move":
        str_orientation = input(f'{self} enter the location you want to place {ship.Ship.name} which is {ship.Ship.length} long in the form row, column: ')
        return Move.from_string(self, str_orientation)

    def place_horizontal(self, player_board: "Board") -> str:
        while True:
            try:
                place = self.get_orientation_horiz()
                place.place_ship_horiz(player_board)
            except MoveError:
                print(MoveError)

    def place_vertical(self, player_board: "Board") -> str:
        while True:
            try:
                place = self.get_orientation_vert()
                place.place_ship_vert(player_board)
            except MoveError:
                print(MoveError)

    def take_turn(self, the_board: "Board") -> None:
        while True:
            try:
                move = self.get_move()
                move.make(the_board)
            except MoveError:
                print(MoveError)

    def get_move(self) -> "Move":
        str_move = input(f'{self} enter the location you want to fire at in the form row, column: ')
        return Move.from_string(self, str_move)
