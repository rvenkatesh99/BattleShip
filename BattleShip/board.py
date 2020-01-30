import typing
from typing import Iterable, List
from .cell import Cell


class Board(object):
    def __init__(self, num_rows: int, num_cols: int, blank_char: str) -> bool:
        self.contents = [[blank_char for col in range(num_cols)] for row in
                         range(num_rows)]  # will yield copies rather than references
        self.blank_char = blank_char

    @property
    def num_rows(self) -> int:
        return len(self.contents)

    @property
    def num_cols(self) -> int:
        return len(self[0])

    def __str__(self) -> str:
        """
          0 1 2 3 4 5 6 7 8 9
        0 * * * * * * * * * *
        1 * * * * * * * * * *
        2 * * * * * * * * * *
        3 * * * * * * * * * *
        4 * * * * * * * * * *
        5 * * * * * * * * * *
        6 * * * * * * * * * *
        7 * * * * * * * * * *
        8 * * * * * * * * * *
        9 * * * * * * * * * *
        :return:
        """
        sep = ' ' * max([len(str(self.num_rows)), len(str(self.num_cols))])
        rep = sep * 2 + sep.join((str(i) for i in range(self.num_cols))) + '\n'
        for row_index, row in enumerate(self):
            rep += str(row_index) + sep + sep.join(row) + '\n'
        return rep

    def __iter__(self) -> Iterable[List[str]]:
        return iter(self.contents)

    def __getitem__(self, index: int) -> List[str]:
        return self.contents[index]

    def is_in_bounds(self, row: int, col: int) -> bool:
        return (0 <= row < self.num_rows and
                0 <= col < self.num_cols)

