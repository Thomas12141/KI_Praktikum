import math
from copy import deepcopy

from Aufgabe3.game_model import Game
from Aufgabe3.player_model import Player, prepare_game
from Aufgabe3.tree_utils import Node


class MinimaxPlayer(Player):
    symbol = None
    other_symbol = None
    count_nodes = 0

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
            return -1
        else:
            return 0

    def get_symbol(self) -> str:
        return self.symbol

    def get_move(self) -> int:
        moves = self.game.get_possible_moves()
        result = -1
        max = -math.inf
        for move in moves:
            copy = deepcopy(self)
            count_nodes += 1
            copy.game.set_move(move, self.symbol)
            if copy.min_value() > max:
                max = copy.min_value()
                
                result = move
        print(count_nodes + " nodes were created")
        return result

    def max_value(self) -> int:
        if self.terminal_test():
            return self.utility()
        moves = self.game.get_possible_moves()
        result = -math.inf
        for move in moves:
            copy = deepcopy(self)
            count_nodes += 1
            copy.game.set_move(move, self.other_symbol)
            result = max(result, copy.min_value())
        return result

    def min_value(self) -> int:
        if self.terminal_test():
            return self.utility()
        moves = self.game.get_possible_moves()
        result = math.inf
        for move in moves:
            copy = deepcopy(self)
            count_nodes += 1
            copy.game.set_move(move, self.symbol)
            result = min(result, copy.max_value())
        return result


