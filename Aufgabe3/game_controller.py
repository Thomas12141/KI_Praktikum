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
    """implementieren eines ConnectFour Game Controllers"""
    pass