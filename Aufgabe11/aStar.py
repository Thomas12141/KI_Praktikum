import heapq
import math
from queue import PriorityQueue

from networkx import Graph


class Node:
    def __init__(self, graph: Graph, symbol: str, path_length=0, parent=None):
        self.graph = graph
        self.symbol = symbol
        self.path_length = path_length
        self.parent = parent

    def heuristic(self):
        if self.parent is None:
            return 0
        x = self.graph.nodes.get(self.parent.symbol).get("x") - self.graph.nodes.get(self.symbol).get("x")
        y = self.graph.nodes.get(self.parent.symbol).get("y") - self.graph.nodes.get(self.symbol).get("y")
        return math.sqrt(x**2 + y**2)*150

    def aStarSearch(start: str, end: str, graph: Graph):
        initial_node = Node(graph, start)
        explored = set()
        frontier = []
        heapq.heappush(frontier, (initial_node.path_length + initial_node.heuristic(), initial_node))

        while frontier:
            current = heapq.heappop(frontier)

            if current.symbol == end:
                return current

            explored.add(current.symbol)
            for neighbor in graph.adj[current]:
                node = Node(graph, neighbor, current.path_length + graph.adj[neighbor][current]["weight"], current)
                if node.symbol not in explored and node not in frontier:
                    heapq.heappush(frontier, (node.path_length + node.heuristic(), node))
                else if
