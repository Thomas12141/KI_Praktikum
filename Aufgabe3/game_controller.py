"""Entwickeln Sie einen ConnectFour Controller der das Spiel durchführt.
Das heißt die Spielzüge ans Spiel weitergibt und den Status des Spiels an die View übergibt"""

from abc import abstractmethod, ABC

from Aufgabe3.board_model import Board
from game_model import Game
from player_model import Player, UniformCostSimplePlayer
from game_view import GameView


class GameController(ABC):
    game: Game
    view: GameView

    def __init__(self, game: Game, view: GameView) -> None:
        self.game = game
        self.view = view
        pass

    @abstractmethod
    def _play_one_round(self, current_player: Player) -> bool:
        pass

    @abstractmethod
    def start(self):
        pass


class GameControllerTicTacToe(GameController):
    """implementieren eines Tic-Tac-Toe Game Controllers"""
    pass


class GameControllerConnectFour(GameController):
    def start(self):
        print("Possible input: digits 0,1,...,6")
        self.view.draw(self.game.board)
        print("  0   1   2   3   4   5   6\n")
        pass
    def _play_one_round(self, current_player: Player) -> bool:
        move = current_player.get_move()
        if self.game.set_move(move, current_player.get_symbol()):
            self.view.draw(self.game.board)
            return True
        return False

    def _play_whole_game(self, current_player: UniformCostSimplePlayer) -> Board:
        return current_player.get_solution()
