
"""geben Sie den Spielzustand auf der Console aus"""

from abc import ABC, abstractmethod

class GameView(ABC):
    @abstractmethod
    def draw(self, board: dict):
        pass


class GameViewTicTacToe(GameView):
    """Tic Tac Toe Game View erstellen"""
    pass

class GameViewConnectFour(GameView):
    """Connect Four Game View erstellen"""
    pass