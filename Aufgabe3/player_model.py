"""Entwickeln Sie unterschiedliche Spieler für ihr TicTacToe Spiel"""
import random
from abc import ABC, abstractmethod

from board_model import Board


class Player(ABC):
    """MVC - MODEL"""

    @abstractmethod
    def get_symbol(self):
        pass

    @abstractmethod
    def get_move(self) -> int:
        pass


class RandomPlayer(Player):
    def __init__(self, symobl, name, board: Board):
        self.symobl = symobl
        self.board = board
        self.name = name

    def get_symbol(self):
        return self.symobl

    def get_move(self) -> int:
        return random.randrange(0, 7, 1)


class HumanPlayer(Player):
    def __init__(self, symbol, name, board: Board):
        self.symbol = symbol
        self.board = board
        self.name = name

    def get_symbol(self):
        return self.symbol

    def get_move(self) -> int:
        move = input("Choose a field for player " + self.name + " (symbol " + self.symbol + ")")
        allowed_moves = [0, 1, 2, 3, 4, 5, 6]
        while not move.isdigit() or int(move) not in allowed_moves:
            input("This field is not allowed. Please try again.")
            move = input("Choose a field for player " + self.name + " (symbol " + self.symbol + ")")
        return int(move)
