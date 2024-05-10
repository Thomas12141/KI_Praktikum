import heapq
import math
from queue import PriorityQueue

from networkx import Graph

from Aufgabe11.saving_graph import creating_graph


def aStarSearch(start: str, end: str, graph: Graph):
    initial_node = Node(graph, start)
    explored = set()
    frontier = []
    heapq.heappush(frontier, (initial_node.path_length + initial_node.heuristic(), initial_node))

    while frontier:
        current = heapq.heappop(frontier)

        if current[1].symbol == end:
            return current

        explored.add(current[1].symbol)
        for neighbor in graph.adj[current[1].symbol]:
            node = Node(graph, neighbor, current[1].path_length + graph.adj[neighbor][current[1].symbol]["weight"],
                        current)
            if node.symbol not in explored and node not in frontier:
                heapq.heappush(frontier, (node.path_length + node.heuristic(), node))
            elif any(node.symbol == other[1].symbol and node.path_length < other[1].path_length for other in frontier):
                index = next(i for i, v in enumerate(frontier) if v.symbol == node.symbol)
                frontier[index] = (node.path_length + node.heuristic(), node)
                heapq.heapify(frontier)


class Node:
    def __init__(self, graph: Graph, symbol: str, path_length=0, parent=None):
        self.graph = graph
        self.symbol = symbol
        self.path_length = path_length
        self.parent = parent

    def heuristic(self):
        if self.parent is None:
            return 0
        x = self.graph.nodes.get(self.parent[1].symbol).get("x") - self.graph.nodes.get(self.symbol).get("x")
        y = self.graph.nodes.get(self.parent[1].symbol).get("y") - self.graph.nodes.get(self.symbol).get("y")
        return math.sqrt(x ** 2 + y ** 2) * 150


print(aStarSearch("a", "c", creating_graph()))
