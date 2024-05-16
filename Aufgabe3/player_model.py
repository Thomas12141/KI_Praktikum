"""Entwickeln Sie unterschiedliche Spieler für ihr TicTacToe Spiel"""
import heapq
import random
from abc import ABC, abstractmethod

from board_model import Board
from game_model import ConnectFour, Game
from tree_utils import Node


def prepare_game(game: Game, first_symbol: str, second_symbol: str):
    # prefill the board for better testing
    player_a = HumanPlayer(first_symbol, "A", game)
    player_b = HumanPlayer(second_symbol, "B", game)
    whos_turn = player_a

    for i in range(2):
        for j in range(5):
            game.set_move(j, whos_turn.symbol)
            whos_turn = player_b if whos_turn == player_a else player_a


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
            possible_moves = self.game.get_possible_moves()
            current_game, cost, moves_made = frontier.pop(0)
            if len(possible_moves) == 1:
                return possible_moves[0]
            if len(frontier) >= 3000:
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


class UniformCostSimplePlayer(Player):
    active_symbol = None
    game = None
    winning_solution = None

    def __init__(self, game: Game):
        self.symbols = ["X", "O"]
        self.active_symbol = self.symbols[0]
        self.game = game

    def uniform_cost_search(self, problem: Game):

        #reduce testing time
        prepare_game(problem, "X", "O")

        initial_node = Node(problem)
        frontier = []
        heapq.heappush(frontier, (initial_node.path_cost, initial_node))
        explored = set()

        while frontier:
            _, node = heapq.heappop(frontier)

            if node.is_goal_state():
                return node

            explored.add(tuple(node.state_tuple()))

            for action in node.actions():
                child = node.child_node(action)
                if child.state_tuple() not in explored and all(
                        child.state_tuple() != other[1].state_tuple() for other in frontier):
                    heapq.heappush(frontier, (child.path_cost, child))
                elif any(
                        child.state_tuple() == other[1].state_tuple() and child.path_cost < other[1].path_cost for other
                        in frontier):
                    index = next(i for i, v in enumerate(frontier) if v[1].state_tuple() == child.state_tuple())
                    frontier[index] = (child.path_cost, child)
                    heapq.heapify(frontier)

        return None  # Keine Lösung gefunden

    def get_symbol(self):
        return self.active_symbol

    def get_move(self) -> int:
        self.active_symbol = self.symbols[0] if self.active_symbol == self.symbols[1] else self.symbols[1]
        if (self.winning_solution):
            next_action = self.winning_solution[0]
            self.winning_solution = self.winning_solution[1:]
            return next_action

        self.winning_node = self.uniform_cost_search(self.game)
        self.winning_solution = self.winning_node.solution()
        return 0

    def get_solution(self) -> Board:
        self.active_symbol = self.symbols[0] if self.active_symbol == self.symbols[1] else self.symbols[1]
        Node = self.uniform_cost_search(self.game)
        return Node.state.board
