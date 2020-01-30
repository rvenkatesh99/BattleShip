from .board import Board

class Ship(object):
    def __init__(self, name, length) -> None:
        self.name = None
        self.char = name[0]
        self.length = None # set by parameters?
        self.health = self.length

    def get_ship_name(self) -> str:
        ship_name = input()
        return ship_name

    def get_ship_initial(self) -> str:
        return self.char

    def if_ship_hit(self) -> int:
        self.health = self.health - 1
        return self.health

    def check_ship_sunk(self) -> bool:
        if self.health == 0:
            return True
        else:
            return False

    def all_ships_destroyed(self) -> bool:
        pass