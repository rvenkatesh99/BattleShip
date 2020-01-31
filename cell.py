class Cell(object):
    def __init__(self, symbol) -> None:
        pass

    def change_to_ship(self) -> str:
        pass

    def change_to_hit(self) -> str:
        return 'X'

    def change_to_miss(self) -> str:
        return 'O'