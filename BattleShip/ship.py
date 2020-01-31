from .board import Board


class Ship(object):
    def __init__(self, name, length) -> None:
        self.name = name
        self.char = name[0]
        self.length = length
        self.health = length

    def if_ship_hit(self) -> int:
        self.health = self.health - 1
        return self.health

    def check_ship_sunk(self) -> bool:
        if self.health == 0:
            return True
        else:
            return False
