from .ship import Ship

class Player(object):
    def __init__(self) -> None:
        self.name = None
        self.ships = None

    def __str__(self) -> str:
        return self.name

    def player_name(self) -> str:
        inputted_name_p1 = input("Player 1 please enter your name:")
        inputted_name_p2 = input("Player 2 please enter your name:")
