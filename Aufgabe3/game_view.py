
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
    def draw(self, board: dict):
        board_string = ""
        for i in range(len(board[0].row) - 1, -1, -1):
            board_string += "\n"
            for row in board:
                board_string += str(row.row[i])
            board_string += "|"
        print(board_string)
        return board_string