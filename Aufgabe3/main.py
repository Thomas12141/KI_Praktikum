from game_controller import GameControllerConnectFour
from board_model import ConnectFourBoard, Cell
from game_model import ConnectFour
from player_model import HumanPlayer, RandomPlayer, UniformCostPlayer, UniformCostSimplePlayer
from game_view import GameViewConnectFour


def main():
    board = ConnectFourBoard()
    game = ConnectFour(board)
    view = GameViewConnectFour()
    player_c = UniformCostSimplePlayer(game)

    controller = GameControllerConnectFour(game, view)
    controller.start()

    whos_turn = player_c
    while True:

        controller._play_one_round(whos_turn)
        if game.check_win(whos_turn.get_symbol()):
            print("The winner is " + whos_turn.get_symbol() + ".")
            break
        if board.is_full():
            print("The game is over, without a winner.")
            break


if __name__ == '__main__':
    main()
