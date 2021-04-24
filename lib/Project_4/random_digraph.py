import random as rng
from lib.Project_1.read_data import print_matrix
from lib.Project_1.random_graph import adj_matrix_init_zero
from .DiMatrixRepresentation import DiMatrixRepresentation
from .plot_digraph_on_circle import plot_digraph_on_circle


def random_graph_probability(num_vertices, probability):
    matrix = adj_matrix_init_zero(num_vertices)
    rng.seed()

    for i in range(num_vertices):
        for j in range(num_vertices):
            if rng.random() <= probability and i != j:
                matrix[i][j] = 1

    return matrix


def digraph_randomizer_start():
    random_graph_adj = []
    num_vertices, probability = input("Podaj liczbe wierzcholkow grafu i prawdopodbienstwo istnienia krawedzi\n> ").split()
    num_vertices = int(num_vertices)
    probability = float(probability)

    random_graph_adj = random_graph_probability(num_vertices, probability)
    print_matrix(random_graph_adj)

    random_graph = DiMatrixRepresentation.AdjacencyMatrix.to_digraph_func()(random_graph_adj)
    plot_digraph_on_circle(random_graph)
