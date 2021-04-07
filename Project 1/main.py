from read_data import read_matrix_from_file
from plot_igraph_on_circle import plot_igraph_on_circle
from matrix_conversions import *
from igraph_creation import *
from MatrixRepresentation import MatrixRepresentation
from random_graph import *


def print_list(list):
    i = 1
    for row in list:
        string = str(i) + ". "
        for x in row:
            string += str(x) + " "
        print(string)
        i += 1


def print_matrix(matrix):
    for row in matrix:
        string = ""
        for x in row:
            string += str(x) + " "
        print(string)


def graph_print(matrix_representation_kind, matrix):
    matrix_representation_out = MatrixRepresentation(int(input("Wskaż format wyjściowy macierzy\n - 0 - lista sąsiedztwa\n - 1 - macierz incydencji\n - 2 - macierz sąsiedztwa\n> ")))
    converted = matrix_representation_kind.convert_func(matrix_representation_out)(matrix)
    if matrix_representation_out == MatrixRepresentation.List:
        print_list(converted)
    else:
        print_matrix(converted)


if __name__ == '__main__':
    confirm_random = input("Czy chcesz wygenerowac graf losowy?    tak/nie\n")
    if confirm_random == "tak":
        random_graph = []
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

    filename = input("Wskaż nazwę pliku zawierającego macierz w formie\n - listy sąsiedztwa\n - macierzy incydencji\n - macierzy sąsiedztwa\n> ")

    matrix, matrix_representation = read_matrix_from_file(filename)
    print("Wykryto " + matrix_representation.to_string())

    graph = matrix_representation.to_igraph_func()(matrix)
    plot_igraph_on_circle(graph)

    graph_print(matrix_representation, matrix)