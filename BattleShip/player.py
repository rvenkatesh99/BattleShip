from .ship import Ship
from typing import Iterable
from .move import Move, MoveError
from .board import Board


class Player(object):
    def __init__(self, other_players: Iterable["Player"], blank_character: str) -> None:
        self.name = self.get_name_from_player(other_players)
        self.ships = self.get_ships_from_player(other_players, blank_character)

    @staticmethod
    def get_name_from_player(other_players: Iterable["Player"]) -> str:
        already_used_names = set([player.name for player in other_players])
        while True:
            name = input('Please enter your name: ')
            if name not in already_used_names:
                return name
            else:
                print(f'{name} has already been used. Pick another name.')

    @staticmethod
    def get_ships_from_player(other_players: Iterable["Player"], blank_character: str) -> str:
        already_used_pieces = set([player.ships for player in other_players])
        while True:
            ship = input('Please enter the ship you want use: ').strip()
            if len(ship) > 1:
                print("You ship may only be a single character. Pick another ship.")
            elif ship == blank_character:
                print(f'You cannot pick {blank_character} for your ship. Pick another ship.')
            elif ship in already_used_pieces:
                print(f'{ship} has already been used. Pick another ship.')
            else:
                return ship

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
        str_move = input(f'{self} enter where you want to play in the form row, col: ')
        return Move.from_string(self, str_move)
