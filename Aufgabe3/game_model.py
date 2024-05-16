"""Entwickeln Sie ein TicTacToe Game das den Spielzustand hällt"""

from abc import ABC, abstractmethod
from board_model import Board, Cell


class Game(ABC):
    """Spiele Daten für zweispieler Spiele und einem Quardratischem Spielfeld"""
    """MVC - MODEL"""
    board: Board

    def __init__(self, board: Board) -> None:
        self.board = board

    @abstractmethod
    def get_status(self):
        pass

    @abstractmethod
    def check_win(self, symbol: str):
        pass

    @abstractmethod
    def set_move(self, x: int, symbol: str) -> bool:
        pass

    @abstractmethod
    def _possible_move(self, x: int) -> bool:
        pass

    @abstractmethod
    def is_board_full(self) -> bool:
        pass

    @abstractmethod
    def copy(self):
        pass

    @abstractmethod
    def get_possible_moves(self):
        pass

    @abstractmethod
    def to_tuple(self):
        pass


class TicTacToe(Game):
    """Implement game hier"""
    pass


class ConnectFour(Game):

    def __init__(self, board: Board) -> None:
        super().__init__(board)

    def get_status(self):
        pass

    def check_win(self, symbol: str):
        check_horizontal = self._check_horizontal(symbol)
        check_vertical = self._check_vertical(symbol)
        check_diagonal = self._check_diagonal(symbol)
        return check_horizontal or check_vertical or check_diagonal

    def _check_horizontal(self, symbol: str) -> bool:
        for row in self.board:
            for i in range(len(row) - 3):
                if row[i].symbol == symbol and row[i + 1].symbol == symbol and row[i + 2].symbol == symbol \
                        and row[i + 3].symbol == symbol:
                    return True
        return False

    def _check_vertical(self, symbol: str) -> bool:
        for i in range(len(self.board) - 3):
            for j in range(len(self.board[0])):
                if self.board[i][j].symbol == (symbol) and self.board[i + 1][j].symbol == symbol and \
                        self.board[i + 2][j].symbol == symbol and self.board[i + 3][j].symbol == symbol:
                    return True
        return False

    def _check_diagonal(self, symbol: str) -> bool:
        for i in range(0, len(self.board) - 3):
            for j in range(0, len(self.board[0]) - 3):
                if self.board[i][j].symbol == symbol and self.board[i + 1][j + 1].symbol == symbol and \
                        self.board[i + 2][j + 2].symbol == symbol and self.board[i + 3][j + 3].symbol == symbol:
                    return True
                if self.board[i][j+3].symbol == symbol and self.board[i + 1][j + 2].symbol == symbol and \
                        self.board[i + 2][j + 1].symbol == symbol and self.board[i + 3][j].symbol == symbol:
                    return True
        return False

    def _possible_move(self, x: int) -> bool:
        return self.board.check_row_is_full(x)

    def set_move(self, x: int, symbol: str) -> bool:
        if self._possible_move(x):
            return False
        self.board.set_cell(x, Cell(symbol))
        return True

    def is_board_full(self) -> bool:
        return self.board.is_full()

    def get_possible_moves(self):
        moves = []
        len = self.board.__len__()
        for i in range(len):
            if self.board.check_row_is_full(i):
                continue
            moves.append(i)
        return moves

    def copy(self):
        return ConnectFour(self.board.copy())

    def to_tuple(self):
        return tuple(tuple(cell.symbol for cell in row) for row in self.board)
