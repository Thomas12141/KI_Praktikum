import json

import networkx as nx
from networkx.readwrite import json_graph

graph = nx.Graph()
graph.add_node("a", city="London")
graph.add_node("b", city="Berlin")
graph.add_node("c", city="Madrid")
graph.add_node("d", city="Kyiv")
graph.add_node("e", city="Rome")
graph.add_node("f", city="Paris")
graph.add_node("g", city="Moscow")
graph.add_node("h", city="Stockholm")
graph.add_node("i", city="Dublin")
graph.add_node("j", city="Bucharest")

graph.add_edge("c", "f", weight=903)
graph.add_edge("c", "e", weight=4092)
graph.add_edge("e", "f", weight=792)
graph.add_edge("e", "j", weight=933)
graph.add_edge("j", "b", weight=1062)
graph.add_edge("j", "d", weight=492)
graph.add_edge("g", "d", weight=627)
graph.add_edge("g", "b", weight=1299)
graph.add_edge("g", "h", weight=819)
graph.add_edge("h", "b", weight=480)
graph.add_edge("h", "a", weight=999)
graph.add_edge("f", "b", weight=735)
graph.add_edge("a", "f", weight=576)
graph.add_edge("a", "i", weight=414)


with open("graph.json", "w") as output_file:
    json.dump(json_graph.adjacency_data(graph), output_file)

