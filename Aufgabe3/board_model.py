"""Entwickeln Sie ein 3x3 TicTacToeBoard"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


@dataclass
class Cell:
    symbol: str = " "

    def __str__(self) -> str:
        return "| " + self.symbol + " "

    def __repr__(self) -> str:
        return self.__str__()


class Row:
    row: List[Cell] = []
    index: int

    def __init__(self, row: List[Cell]) -> None:
        self.row = row
        self.index = 0

    def set_cell(self, value: Cell) -> None:
        if self.check_row_is_full():
            return
        self.row[self.index] = value
        self.index += 1

    def check_row_is_full(self) -> bool:
        return self.index >= len(self.row)

    def __str__(self) -> str:
        return "|".join([cell.symbol for cell in self.row])

    def __repr__(self) -> str:
        return self.__str__()

    def __len__(self):
        return len(self.row)

    def __setitem__(self, key, value):
        ##self.row[key] = value
        ## use set_cell instead (index is used to set the cell)
        self.set_cell(value)

    def __getitem__(self, key):
        return self.row[key]


class Board(ABC):

    @abstractmethod
    def _init_board(self):
        pass

    @abstractmethod
    def get_cell_value(self, index: int) -> str:
        pass

    @abstractmethod
    def set_cell(self, index: int) -> bool:
        pass

    @abstractmethod
    def check_row_is_full(self, index: int) -> bool:
        pass

    def __str__(self) -> str:
        return "Das ist das Board für das Spiel " + self.game_name

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __setitem__(self, key, value):
        self.dic[key] = value

    @abstractmethod
    def __getitem__(self, key):
        return self.dic[key]


class TicTacToeBoard(Board):
    """implementieren eines Tic-Tac-Toe Spielfeldes"""
    pass


class ConnectFourBoard(Board):
    """implementieren eines ConnectFour Spielfeldes"""

    board: List[Row]

    def __init__(self) -> None:
        self.game_name = "ConnectFour"
        self._init_board()

    def _init_board(self):
        self.board = [Row([Cell(symbol=" ") for _ in range(6)]) for _ in range(7)]

    def get_cell_value(self, index: int) -> str:
        return self.board[index]

    def check_row_is_full(self, index: int) -> bool:
        return self.board[index].check_row_is_full()

    def set_cell(self, index: int, value: Cell) -> bool:
        return self.board[index].set_cell(value)

    def __iter__(self):
        return iter(self.board)

    def __len__(self):
        return len(self.board)

    def __setitem__(self, key, value):
        self.board[key] = value

    def __getitem__(self, key):
        return self.board[key]

    def print_board(self):
        board_string = ""
        for i in range(len(self.board[0].row) - 1, -1, -1):
            board_string += "\n"
            for row in self.board:
                board_string += str(row.row[i])
            board_string += "|"
        print(board_string)






