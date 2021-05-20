from lib.Project_1.MatrixRepresentation import MatrixRepresentation
import random

import numpy as np

from lib.Project_1.matrix_conversions import adjacency_matrix_to_list
from lib.Project_1.random_graph import random_graph_edges, random_graph_probability
from lib.Project_1.read_data import read_matrix_from_file
from lib.Utils.decorators import retry_on_value_error
from lib.Project_2.largest_connected_component import components


# returns result in form of adjacency matrix
def subgraph_from_list_of_vertices(original_adjacency_matrix, vertices_list):
    adjacency_indexes = sorted([v-1 for v in vertices_list])
    size = len(vertices_list)
    res = [[0] * size for _ in range(size)]
    for i in range(0, size):
        v1 = adjacency_indexes[i]
        for j in range(0, i):
            v2 = adjacency_indexes[j]
            res[i][j] = original_adjacency_matrix[v1][v2]
    return res


# generates random adjacency matrix based on input from the user
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


# returns resulting adjacency matrix
def retrieve_largest_component(adjacency_matrix):
    if len(adjacency_matrix) == 0:
        return None
    c = components(adjacency_matrix_to_list(adjacency_matrix))
    largest = max(c, key=len)
    return subgraph_from_list_of_vertices(adjacency_matrix, largest)


# returns resulting adjacency matrix
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


# returns resulting adjacency matrix
# if graph is not connected will automatically extract largest connected component
def generate_random_weighted_graph_adjacency(arg_singleton):
    args = arg_singleton.get_instance().arguments
    if args['filename'] is None:
        adjacency_matrix_initial = retrieve_random_graph_from_user()
    else:
        [adjacency_matrix_initial, representation] = read_matrix_from_file(args['filename'])
        if representation != MatrixRepresentation.AdjacencyMatrix:
            raise ValueError("Program oczekuje macierzy sasiedztwa")
            
    largest_connected = np.array(retrieve_largest_component(adjacency_matrix_initial))
    if largest_connected.size == 1:  # discard empty graph
        return None
    adjacency_matrix = assign_weights_to_graph(largest_connected, 1, 10)
    return adjacency_matrix
