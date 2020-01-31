from . import ship
from typing import Iterable
from .move import Move, MoveError
from .board import Board

# ship list within the player class

class Player(object):
    def __init__(self, name, other_players: Iterable["Player"], blank_character: str = "*") -> None:
        self.name = self.get_name_from_player(other_players)
        self.ship_orient = self.get_ship_orientation(other_players, blank_character)
        self.player_ships = ship.Ship()

    @staticmethod
    def get_name_from_player(other_players: Iterable["Player"]) -> str:
        already_used_names = set([player.name for player in other_players])
        while True:
            name = input('Please enter your name: ')
            if name not in already_used_names:
                return name
            else:
                print(f'{name} has already been used. Pick another name.')

    def place_horizontal(self) -> str:
        pass

    def place_vertical(self) -> str:
        pass

    @staticmethod
    def get_ship_orientation(self, other_players: Iterable["Player"], blank_character: str) -> str:
        already_used_ships = set([player.ships for player in other_players])
        while True:
            ship_h_or_v = input(
                f'{self.name} Enter horizontal or vertical for the placement of {ship.Ship.name} which is {ship.Ship.length} long').strip()
            ship_h_or_v = ship_h_or_v.lower()
            if str.startswith(ship_h_or_v) == "h":
                return self.place_horizontal()
            elif str.startswith(ship_h_or_v) == "v":
                return self.place_vertical()
            else:
                print("That was not a valid orientation. Enter")

    def __str__(self) -> str:
        return self.name

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
