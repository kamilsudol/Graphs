import matplotlib.pyplot as plt


def get_weighed_edges(graph, weights):
    edges = []
    for i, row in enumerate(graph):
        edges += [[i, j, weights[i][j]] for j in range(len(graph[0])) if graph[i][j]]
    return edges


def plot_weighted_edges(vertices, es):
    for i, edge in enumerate(es):
        (x1, y1) = vertices[edge[0]][0:2]
        (x2, y2) = vertices[edge[1]][0:2]
        shift_x = (x2 - x1) * 0.77
        shift_y = (y2 - y1) * 0.77
        plt.annotate(int(edge[2]), (x1 + shift_x, y1 + shift_y))