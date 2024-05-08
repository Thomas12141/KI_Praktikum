import math
from copy import deepcopy

from Aufgabe3.game_model import Game
from Aufgabe3.player_model import Player, prepare_game
from Aufgabe3.tree_utils import Node


class MinimaxPlayer(Player):
    symbol = None
    other_symbol = None

    def __init__(self, game: Game, symbol: str, other_symbol: str):
        self.symbol = symbol
        self.other_symbol = other_symbol
        self.game = game

    def terminal_test(self) -> bool:
        return self.game.check_win(self.symbol) or self.game.check_win(
            self.other_symbol) or self.game.is_board_full()

    def utility(self) -> int:
        if self.game.check_win(self.symbol):
            return 1
        elif self.game.check_win(self.other_symbol):
            return 0
        else:
            return -1

    def get_symbol(self) -> str:
        return self.symbol

    def get_move(self) -> int:
        moves = self.game.get_possible_moves()
        result = -1
        min = math.inf
        for move in moves:
            copy = deepcopy(self)
            copy.game.set_move(move, self.symbol)
            if copy.min_value() < min:
                min = copy.min_value()
                result = move
        return result

    def max_value(self) -> int:
        if self.terminal_test():
            return self.utility()
        moves = self.game.get_possible_moves()
        result = -math.inf
        for move in moves:
            copy = deepcopy(self)
            copy.game.set_move(move, self.symbol)
            result = max(result, copy.min_value())
        return result

    def min_value(self) -> int:
        if self.terminal_test():
            return self.utility()
        moves = self.game.get_possible_moves()
        result = math.inf
        for move in moves:
            copy = deepcopy(self)
            copy.game.set_move(move, self.symbol)
            result = min(result, copy.max_value())
        return result


