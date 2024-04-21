"""Entwickeln Sie unterschiedliche Spieler für ihr TicTacToe Spiel"""
import random
from abc import ABC, abstractmethod

from game_model import ConnectFour, Game
from board_model import Board, Cell


class Player(ABC):
    """MVC - MODEL"""

    @abstractmethod
    def get_symbol(self):
        pass

    @abstractmethod
    def get_move(self) -> int:
        pass


class RandomPlayer(Player):
    def __init__(self, symobl, name, game: Game):
        self.symobl = symobl
        self.name = name

    def get_symbol(self):
        return self.symobl

    def get_move(self) -> int:
        return random.randrange(0, 7, 1)


class HumanPlayer(Player):
    def __init__(self, symbol, name, game: Game):
        self.symbol = symbol
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
    
class UniformCostPlayer(Player):
    
    active_symbol = None
    game = None
        
    def __init__(self, game: Game):
        self.symbols = ["X", "O"]
        self.active_symbol = self.symbols[0]
        self.game = game
        
    def generate_possible_moves(self):
        moves = []
        len = self.game.board.__len__()
        for i in range(len):
            if self.game.board.check_row_is_full(i):
                continue
            moves.append(i)
        return moves
    
    
    
    def evaluate(self, game: Game, symbol: str) -> int:
        
        if game.check_win(symbol):
            return 100
        
        return 0
    
    def uniform_cost_search(self):
        frontier = [(self.game, 0, [])]
        while frontier:
            possible_moves = self.generate_possible_moves()
            current_game, cost, moves_made = frontier.pop(0)
            if len(possible_moves) == 1:
                return possible_moves[0]
            if len(frontier) >= 6000:
                return moves_made[-1]
            for move in possible_moves:
                new_game = self.game.copy()
                new_game.set_move(move, self.active_symbol)
                evaluate_score = self.evaluate(new_game, self.active_symbol)
                frontier.append((new_game, cost + 1 + evaluate_score, moves_made + [move]))
                frontier.sort(key=lambda x: x[1])
        return None

    def get_symbol(self):
        return self.active_symbol
    def get_move(self) -> int:
        self.active_symbol = self.symbols[0] if self.active_symbol == self.symbols[1] else self.symbols[1]
        return self.uniform_cost_search()
