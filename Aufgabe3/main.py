from board_model import ConnectFourBoard
from game_model import ConnectFour
from player_model import HumanPlayer, RandomPlayer
from game_view import GameViewConnectFour


def main():
    board = ConnectFourBoard()
    game = ConnectFour(board)
    print("Possible input: digits 0,1,...,6")
    board.print_board()
    print("  0   1   2   3   4   5   6\n")
    player_a = HumanPlayer("X", "A", board)
    player_b = RandomPlayer("O", "B", board)
    whos_turn = player_a
    turn_player_a = True
    while True:
        if turn_player_a:
            whos_turn = player_a
            turn_player_a = False
        else:
            whos_turn = player_b
            turn_player_a = True
        while not game.set_move(whos_turn.get_move(), whos_turn.get_symbol()):
            match whos_turn:
                case HumanPlayer():
                    print("This row is full. Please try again.")
        board.print_board()
        if game.check_win(whos_turn.get_symbol()):
            print("The winner is " + whos_turn.get_symbol() + ".")
            break
        if board.is_full():
            print("The game is over, without a winner.")
            break


if __name__ == '__main__':
    main()
