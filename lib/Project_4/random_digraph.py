import random as rng
from lib.Project_1.read_data import print_matrix
from lib.Project_1.random_graph import adj_matrix_init_zero
from .DiMatrixRepresentation import DiMatrixRepresentation
from .plot_digraph_on_circle import plot_digraph_on_circle
from lib.Utils.decorators import retry_on_value_error


def random_graph_probability(num_vertices, probability):
    matrix = adj_matrix_init_zero(num_vertices)
    rng.seed()

    for i in range(num_vertices):
        for j in range(num_vertices):
            if rng.random() <= probability and i != j:
                matrix[i][j] = 1

    return matrix


@retry_on_value_error
def input_vertices_and_probability():
    num_vertices, probability = input("Podaj liczbe wierzcholkow grafu i prawdopodbienstwo istnienia krawedzi\n> ").split()
    num_vertices, probability = int(num_vertices), float(probability)

    if num_vertices < 0:
        raise ValueError("Liczba wierzcholkow nie moze byc ujemna")
 
    if not 0 <= probability <= 1:
        raise ValueError("Prawdopodobienstwo musi byc w przedziale [0, 1]")

    return num_vertices, probability


#return adjacency matrix
def generate_random_digraph():
    num_vertices, probability = input_vertices_and_probability()
    return random_graph_probability(num_vertices, probability)


def digraph_randomizer_start():
    random_graph_adj = generate_random_digraph()
    print_matrix(random_graph_adj)

    random_graph = DiMatrixRepresentation.AdjacencyMatrix.to_digraph_func()(random_graph_adj)
    plot_digraph_on_circle(random_graph)
