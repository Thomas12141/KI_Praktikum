
class Node:
    def __init__(self, symbol: str, path_length=0, parent=None):
        self.symbol = symbol
        self.path_length = path_length
        self.parent = parent
