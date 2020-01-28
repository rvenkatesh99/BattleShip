from .ship import Ship

class Player(object):
    def __init__(self) -> None:
        self.name = None
        self.ships = None

    def __str__(self) -> str:
        return self.name
