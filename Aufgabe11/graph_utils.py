import math


class GraphNode :
    def __init__(self, key, city, pos_x, pos_y):
        self.key = key
        self.city = city
        self.pos_x = pos_x
        self.pos_y = pos_y

    def __str__(self):
        return self.city
    
class GraphEdge :
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

    def __str__(self):
        return self.start + " -> " + self.end + ": " + str(self.weight)
    
class Graph :
    def __init__(self):
        self.nodes = []
        self.edges = []
        
    def add_node(self, key, city, x, y):
        self.nodes.append(GraphNode(key, city, x, y))
        
    def add_edge(self, start, end, weight):
        self.edges.append(GraphEdge(start, end, weight))
        
    def get_node(self, key):
        for node in self.nodes:
            if node.key == key:
                return node
        return None
    
    def get_edge(self, start, end):
        for edge in self.edges:
            if edge.start == start and edge.end == end:
                return edge
        return None
    
    def get_neighbors(self, key):
        neighbors = []
        for edge in self.edges:
            if edge.start == key:
                neighbors.append(edge.end)
        return neighbors
    
    def get_edge_weight(self, start, end):
        edge = self.get_edge(start, end)
        
        if edge is not None:
            return edge.weight 
        return None
    
    def get_heuristic(self, start, end):
        node_start = self.get_node(start)
        node_end = self.get_node(end)
        x = node_start.pos_x - node_end.pos_x
        y = node_start.pos_y - node_end.pos_y
        return math.sqrt(x ** 2 + y ** 2) * 0
    
    def __str__(self):
        result = ""
        for node in self.nodes:
            result += node.city + " (" + str(node.pos_x) + ", " + str(node.pos_y) + ")\n"
        for edge in self.edges:
            result += edge.start + " -> " + edge.end + ": " + str(edge.weight) + "\n"
        return result