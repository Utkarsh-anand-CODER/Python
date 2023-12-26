import random
import itertools
import networkx as nx
import matplotlib.pyplot as plt

def is_valid_coloring(graph, coloring):
    for u, v in graph.edges():
        if coloring[u] == coloring[v]:
            return False
    return True

def greedy_coloring(graph):
    coloring = {}
    for node in graph.nodes():
        adjacent_colors = {coloring.get(neighbor) for neighbor in graph.neighbors(node)}
        coloring[node] = next(color for color in itertools.count() if color not in adjacent_colors)
    return coloring

def generate_random_graph(n_nodes, edge_probability):
    G = nx.Graph()
    G.add_nodes_from(range(n_nodes))

    for i in range(n_nodes):
        for j in range(i + 1, n_nodes):
            if random.random() < edge_probability:
                G.add_edge(i, j)

    return G

# User input
n_nodes = int(input("Enter the number of nodes: "))
edge_probability = float(input("Enter the edge probability (between 0 and 1): "))

G = generate_random_graph(n_nodes, edge_probability)

coloring_result = greedy_coloring(G)

print('Coloring:', coloring_result)
print('Valid:', is_valid_coloring(G, coloring_result))
print('K:', len(set(coloring_result.values())))

color_map = [coloring_result[node] for node in G.nodes()]
nx.draw(G, node_color=color_map, with_labels=True, font_weight='bold')
plt.show()
