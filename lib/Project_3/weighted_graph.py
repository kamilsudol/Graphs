import matplotlib.pyplot as plt

from lib.Project_1.plot_igraph_on_circle import normalize_plot
from lib.Project_1.plot_igraph_on_circle import plot_vertices
from lib.Project_1.plot_igraph_on_circle import span_vertices_on_circle


def get_weighed_edges_list_from_adjacency(matrix):
    edges = []
    for i, row in enumerate(matrix):
        edges += [[i, j, matrix[i][j]] for j in range(i, len(matrix[0])) if matrix[i][j]]
    return edges


def plot_weighted_edges(vertices, es):
    for i, edge in enumerate(es):
        (x1, y1) = vertices[edge[0]][0:2]
        (x2, y2) = vertices[edge[1]][0:2]
        plt.plot((x1, x2), (y1, y2))
        shift_x = (x2 - x1) * 0.3
        shift_y = (y2 - y1) * 0.3
        plt.annotate(int(edge[2]), (x1 + shift_x, y1 + shift_y))


def plot_weighted_graph_on_circle(adjacency_matrix, colormap=None):
    fig, ax = plt.subplots()

    vertices = span_vertices_on_circle(len(adjacency_matrix))
    plot_vertices(vertices, ax, colormap)
    plot_weighted_edges(vertices, get_weighed_edges_list_from_adjacency(adjacency_matrix))

    normalize_plot(ax)
    plt.axis('off')
    plt.show()
