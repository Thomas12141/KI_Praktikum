import heapq
import math
from queue import PriorityQueue

from graph_utils import Graph
from saving_graph import creating_graph


def aStarSearch(start: str, end: str, graph: Graph):
    initial_node = Node(graph, start)
    explored = set()
    frontier = []
    heapq.heappush(frontier, initial_node)
    while frontier:
        node = heapq.heappop(frontier)
        if node.symbol == end:
            return node.path_length, node
        explored.add(node.symbol)
        for neighbor in graph.get_neighbors(node.symbol):
            if neighbor not in explored:
                child = Node(graph, neighbor, node)
                heapq.heappush(frontier, child)
    return None

class Node:
    def __init__(self, graph: Graph, symbol: str, parent=None):
        self.symbol = symbol
        self.parent = parent
        self.path_length = 0
        if parent is not None:
            self.path_length = parent.path_length + graph.get_edge_weight(parent.symbol, symbol)

    def __lt__(self, other):
        return self.path_length < other.path_length

    def __eq__(self, other):
        return self.symbol == other.symbol

    

print("Wo möchtest du starten?")
start = input()
print("Wohin willst du fahren?")
end = input()
iterator = aStarSearch(start, end, creating_graph())

if(iterator is None):
    print("There is no route between the two cities")
    exit(0)

length = iterator[1].path_length

iterator = iterator[1]

queue = []

while iterator.parent is not None:
    queue.append(iterator)
    iterator = iterator.parent
queue.append(iterator)
string = "The length is: " + str(length) + "\nThe best route is: " + queue.pop().symbol

queue.reverse()


for node in queue:
    string += " -> " + node.symbol

print(string)
