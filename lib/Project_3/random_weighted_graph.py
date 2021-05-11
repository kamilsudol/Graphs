import random

import numpy as np
from igraph import *

from lib.Project_1.random_graph import random_graph_edges, random_graph_probability
from lib.Utils.decorators import retry_on_value_error

@retry_on_value_error
def retrieve_random_graph_from_user():
    input_type = int(input('Wpisz 1 aby wylosowac graf G(n, l).\n'
                            'Wpisz 2 aby wylosowac graf G(n, p).\n').strip())

    if input_type == 1:
        nv = int(input('Podaj ilosc wezlow: ').strip())
        ne = int(input('Podaj ilosc krawedzi: ').strip())
        return random_graph_edges(nv, ne)
    elif input_type == 2:
        nv = int(input('Podaj ilosc wezlow: ').strip())
        p = float(input('Podaj prawdopodobienstwo istnienia krawedzi: ').strip())
        return random_graph_probability(nv, p)
    else:
        raise ValueError


def retrieve_largest_component(adjacency_matrix):
    g = Graph.Adjacency(adjacency_matrix)
    if len(adjacency_matrix) == 0:
        return None
    largest = g.clusters().giant()
    return [i for i in largest.get_adjacency()]


def assign_weights_to_graph(adjacency_matrix, min_weight, max_weight):
    random.seed()
    (nonzero_i, nonzero_j) = np.nonzero(adjacency_matrix)
    size = len(adjacency_matrix[0])
    result = np.zeros((size, size))
    for k in range(nonzero_i.size):
        i = nonzero_i[k]
        j = nonzero_j[k]
        result[i][j] = result[j][i] = random.randrange(min_weight, max_weight + 1)
    return result.tolist()


def generate_random_weighted_graph_adjacency():
    adjacency_matrix_initial = retrieve_random_graph_from_user()
    largest_connected = np.array(retrieve_largest_component(adjacency_matrix_initial))
    if largest_connected.size == 1:  # discard empty graph
        return None
    adjacency_matrix = assign_weights_to_graph(largest_connected, 1, 10)
    return adjacency_matrix
