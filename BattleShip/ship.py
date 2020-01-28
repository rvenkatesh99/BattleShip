class Ship(object):
    def __init__(self, name, length, char, health, orientation) -> None:
        self.name = None
        self.char = name[0]
        self.length = None # set by parameters?
        self.health = length

    def ship_hit(self) -> int:

    def ship_sunk(self) -> bool:
        if self.health == 0:
            return True
        else:
            return False
    def all_ships_destroyed(self) -> bool:
        pass