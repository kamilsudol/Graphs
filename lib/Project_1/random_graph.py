import random as rng
from .read_data import graph_print
from .plot_igraph_on_circle import plot_igraph_on_circle
from .MatrixRepresentation import MatrixRepresentation


def adj_matrix_init_zero(num_vertices):
    matrix = []

    for i in range(num_vertices):
        matrix.insert(i, [])
        for j in range(num_vertices):
            matrix[i].append(0)

    return matrix


def random_graph_edges(num_vertices, num_edges):
    if num_edges > num_vertices * (num_vertices - 1) / 2:
        num_edges = int(num_vertices * (num_vertices - 1) / 2)
    matrix = adj_matrix_init_zero(num_vertices)
    rng.seed()

    for x in range(num_edges):
        row = rng.randint(1, num_vertices - 1)
        col = rng.randint(0, row - 1)

        while matrix[row][col] != 0:
            row = rng.randint(1, num_vertices - 1)
            col = rng.randint(0, row - 1)

        matrix[row][col] = 1
        matrix[col][row] = 1

    return matrix


def random_graph_probability(num_vertices, probability):
    matrix = adj_matrix_init_zero(num_vertices)
    rng.seed()

    for i in range(num_vertices):
        for j in range(i):
            if rng.random() <= probability:
                matrix[i][j] = 1
                matrix[j][i] = 1

    return matrix


def graph_randomizer_start():
    random_graph_adj = []
    num_vertices = int(input("Podaj liczbe wierzcholkow grafu.\n"))
    random_method = input("Podaj metode generacji grafu [G(n, l) czy G(n, p)].    l/p\n")
    if random_method == "l":
        num_edges = int(input("Podaj liczbe krawedzi grafu.\n"))
        random_graph_adj = random_graph_edges(num_vertices, num_edges)
    elif random_method == "p":
        probability = float(input("Podaj prawdopodbienstwo istnienia krawedzi.\n"))
        random_graph_adj = random_graph_probability(num_vertices, probability)

    graph_print(MatrixRepresentation.AdjacencyMatrix, random_graph_adj)

    random_graph = MatrixRepresentation.AdjacencyMatrix.to_igraph_func()(random_graph_adj)
    plot_igraph_on_circle(random_graph)
