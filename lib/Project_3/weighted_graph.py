from igraph import *
import matplotlib.pyplot as plt

from lib.Project_1.plot_igraph_on_circle import plot_vertices
from lib.Project_1.plot_igraph_on_circle import span_vertices_on_circle
from lib.Project_1.plot_igraph_on_circle import normalize_plot


def get_weighed_edges_list_from_adjacency(matrix):
    edges = []
    for i, row in enumerate(matrix):
        edges += [[i, j, matrix[i][j]] for j in range(i, len(row)) if matrix[i][j]]
    return edges


def create_weighted_igraph_from_adjacency(matrix):
    g = Graph.TupleList(get_weighed_edges_list_from_adjacency(matrix), weights=True)
    return g


def plot_weighted_edges(vertices, es):
    for i, edge in enumerate(es):
        print(es['weight'])
        (x1, y1) = vertices[edge.source][0:2]
        (x2, y2) = vertices[edge.target][0:2]
        plt.plot((x1, x2), (y1, y2))
        shift_x = (x2 - x1) * 0.3
        shift_y = (y2 - y1) * 0.3
        plt.annotate(es['weight'][i], (x1 + shift_x, y1 + shift_y))


def plot_weighted_igraph_on_circle(g, colormap=None):
    fig, ax = plt.subplots()

    vertices = span_vertices_on_circle(g.vcount())
    plot_vertices(vertices, ax, colormap)
    plot_weighted_edges(vertices, g.es)

    normalize_plot(ax)
    plt.axis('off')
    plt.show()
