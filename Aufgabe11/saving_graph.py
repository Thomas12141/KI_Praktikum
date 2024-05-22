import json

import networkx as nx
from networkx.readwrite import json_graph


def creating_graph() -> nx.Graph:
    graph = nx.Graph()
    graph.add_node("a", city="London", x=2, y=7)
    graph.add_node("b", city="Berlin", x=5, y=5)
    graph.add_node("c", city="Madrid", x=0, y=0)
    graph.add_node("d", city="Kyiv", x=9, y=5)
    graph.add_node("e", city="Rome", x=5, y=0)
    graph.add_node("f", city="Paris", x=4, y=3)
    graph.add_node("g", city="Moscow", x=10, y=10)
    graph.add_node("h", city="Stockholm", x=6, y=9)
    graph.add_node("i", city="Dublin", x=1, y=8)
    graph.add_node("j", city="Bucharest", x=8, y=4)

    graph.add_edge("c", "f", weight=903)
    graph.add_edge("f", "c", weight=903)
    graph.add_edge("c", "e", weight=4092)
    graph.add_edge("e", "c", weight=4092)
    graph.add_edge("e", "f", weight=792)
    graph.add_edge("f", "e", weight=792)
    graph.add_edge("e", "j", weight=933)
    graph.add_edge("j", "e", weight=933)
    graph.add_edge("j", "b", weight=1062)
    graph.add_edge("b", "j", weight=1062)
    graph.add_edge("j", "d", weight=492)
    graph.add_edge("d", "j", weight=492)
    graph.add_edge("g", "d", weight=627)
    graph.add_edge("d", "g", weight=627)
    graph.add_edge("g", "b", weight=1299)
    graph.add_edge("b", "g", weight=1299)
    graph.add_edge("g", "h", weight=819)
    graph.add_edge("h", "g", weight=819)
    graph.add_edge("h", "b", weight=480)
    graph.add_edge("b", "h", weight=480)
    graph.add_edge("h", "a", weight=999)
    graph.add_edge("a", "h", weight=999)
    graph.add_edge("f", "b", weight=735)
    graph.add_edge("b", "f", weight=735)
    graph.add_edge("a", "f", weight=576)
    graph.add_edge("f", "a", weight=576)
    graph.add_edge("a", "i", weight=414)
    graph.add_edge("i", "a", weight=414)
    return graph

