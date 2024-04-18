"""Entwickeln Sie einen ConnectFour Controller der das Spiel durchführt.
Das heißt die Spielzüge ans Spiel weitergibt und den Status des Spiels an die View übergibt"""

from abc import abstractmethod, ABC
from game_model import Game
from player_model import Player
from game_view import GameView


class GameController(ABC):
    game: Game
    view: GameView
    player1: Player
    player2: Player

    def __init__(self, game: Game, view: GameView, player1: Player, player2: Player) -> None:
        self.game = game
        self.view = view
        self.player1 = player1
        self.player2 = player2
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