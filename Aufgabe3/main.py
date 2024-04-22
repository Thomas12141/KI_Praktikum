from game_controller import GameControllerConnectFour
from board_model import ConnectFourBoard, Cell
from game_model import ConnectFour
from player_model import HumanPlayer, RandomPlayer, UniformCostPlayer, UniformCostSimplePlayer
from game_view import GameViewConnectFour


def main():
    board = ConnectFourBoard()
    game = ConnectFour(board)
    view = GameViewConnectFour()
    player_a = HumanPlayer("X", "A", game)
    player_b = HumanPlayer("O", "B", game)
    whos_turn = player_a

    controller = GameControllerConnectFour(game, view)
    controller.start()
    for j in range(7):
        for i in range(j, 1+j):
            game.set_move(i, whos_turn.symbol)
            game.set_move(i, whos_turn.symbol)
            whos_turn = player_b if whos_turn == player_a else player_a
            game.set_move(i, whos_turn.symbol)
            game.set_move(i, whos_turn.symbol)
            whos_turn = player_b if whos_turn == player_a else player_a
            game.set_move(i, whos_turn.symbol)
        whos_turn = player_b if whos_turn == player_a else player_a
    game.set_move(0, player_b.symbol)
    game.set_move(1, player_a.symbol)
    view.draw(controller.game.board)
    player_c = UniformCostSimplePlayer(game)

    board = controller._play_whole_game(player_c)
    view.draw(board)
    '''whos_turn = player_c
    while True:
        #whos_turn = player_a if whos_turn == player_b else player_b

        controller._play_one_round(whos_turn)
        if game.check_win(whos_turn.get_symbol()):
            print("The winner is " + whos_turn.get_symbol() + ".")
            break
        if board.is_full():
            print("The game is over, without a winner.")
            break'''


if __name__ == '__main__':
    main()
