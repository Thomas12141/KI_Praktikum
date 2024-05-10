from Aufgabe8.minimax import MinimaxPlayer
from game_controller import GameControllerConnectFour
from board_model import ConnectFourBoard, Cell
from game_model import ConnectFour
from player_model import HumanPlayer, RandomPlayer, UniformCostPlayer, UniformCostSimplePlayer, prepare_game
from game_view import GameViewConnectFour


def main():
    board = ConnectFourBoard()
    game = ConnectFour(board)
    view = GameViewConnectFour()
    player_a = HumanPlayer("X", "Thomas", game)
    player_b = MinimaxPlayer(game,"O", "X")
    prepare_game(game, "X", "O")
    controller = GameControllerConnectFour(game, view)
    whos_turn = player_a
    while True:
        view.draw(board)
        controller._play_one_round(whos_turn)
        if game.check_win(whos_turn.get_symbol()):
            print("The winner is " + whos_turn.get_symbol() + ".")
            break
        if board.is_full():
            print("The game is over, without a winner.")
            break
        whos_turn = player_a if whos_turn == player_b else player_b

if __name__ == '__main__':
    main()
