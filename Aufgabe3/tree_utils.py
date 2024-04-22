import math

from game_model import Game


class Node:
    def __init__(self, state : Game, parent=None, action=None, path_cost=0, symbol='X'):
        self.state = state  
        self.parent = parent  
        self.action = action  
        self.path_cost = path_cost  
        self.symbol = symbol 

    def actions(self):
        return self.state.get_possible_moves()

    def result(self, action):
        new_state = self.state.copy()
        new_state.set_move(action, self.symbol)
        return new_state

    def is_goal_state(self):
        return self.state.is_board_full()

    def child_node(self, action):
        new_path_cost = None
        new_state = self.result(action)
        if new_state.check_win(self.symbol):
            new_path_cost = math.inf
        else:
            new_path_cost = self.path_cost + 1
        
        next_symbol = 'O' if self.symbol == 'X' else 'X'
        
        return Node(new_state, parent=self, action=action, path_cost=new_path_cost, symbol=next_symbol)

    def state_tuple(self):
        return self.state.to_tuple()
    
    def __lt__(self, other):
        return self.path_cost < other.path_cost

    def __eq__(self, other : 'Node'):
        return self.state_tuple() == other.state_tuple()

    def solution(self):
        solution = []
        node = self
        while node.parent is not None:
            solution.append(node.action)
            node = node.parent
        solution.reverse()  
        return solution