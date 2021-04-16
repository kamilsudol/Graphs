import lib.Project_2.graphic_sequence as gseq

import random as rng
import numpy as np

from lib.Project_1.matrix_conversions import adjacency_matrix_to_incidence_matrix
from lib.Project_1.igraph_creation import create_igraph_from_incidence_matrix
from lib.Project_1.plot_igraph_on_circle import plot_igraph_on_circle


def roll_edges(inc, num_vertices):
    rng.seed()

    edge_one_col = -1
    edge_two_col = -1
    edge_one_vertices = [-1, -1]
    edge_two_vertices = [-1, -1]

    while edge_one_col == edge_two_col or edge_one_vertices[0] == edge_two_vertices[1] or edge_one_vertices[1] == edge_two_vertices[0]:
        # print("roll edges\n")
        edge_one_col = rng.randint(0, num_vertices)
        edge_two_col = rng.randint(0, num_vertices)

        edge_one_vertices = find_vertices(num_vertices, inc, edge_one_col)
        edge_two_vertices = find_vertices(num_vertices, inc, edge_two_col)
        # print("col1:" + str(edge_one_col) + str(edge_one_vertices))
        # print("col2:" + str(edge_two_col) + str(edge_two_vertices))

    return [edge_one_col, edge_two_col, edge_one_vertices, edge_two_vertices]

def swap_between_columns(row, col1, col2, matrix):
    temp = matrix[row][col1]
    matrix[row][col1] = matrix[row][col2]
    matrix[row][col2] = temp


def find_vertices(num_vertices, inc_matrix, edge_index):
    vertices = [-1, -1]
    for row in range(num_vertices):
        if inc_matrix[row][edge_index] == 1:
            if vertices[0] == -1:
                vertices[0] = row
            else:
                vertices[1] = row
    return vertices


def randomize_edges(graphic_seq, num_shuffles):
    adj = gseq.is_graphic_sequence(graphic_seq)
    is_graphic = False

    if adj is not False:
        is_graphic = True
        num_vertices = len(graphic_seq)
        
        # graph = gseq.create_igraph_from_adjacency_matrix(adj)
        # gseq.plot_igraph_on_circle(graph)

        inc = adjacency_matrix_to_incidence_matrix(adj)
        
        for i in range(num_shuffles):
            edge_one_col, edge_two_col, edge_one_vertices, edge_two_vertices = roll_edges(inc, num_vertices)

            if edge_one_vertices[0] == edge_two_vertices[0]:
                swap_between_columns(edge_one_vertices[1], edge_one_col, edge_two_col, inc)
                swap_between_columns(edge_two_vertices[1], edge_one_col, edge_two_col, inc)
            else:
                swap_between_columns(edge_one_vertices[0], edge_one_col, edge_two_col, inc)
                swap_between_columns(edge_two_vertices[0], edge_one_col, edge_two_col, inc)

        return [is_graphic, inc]
    else:
        return [is_graphic, []]


def test_randomization():
    num_shuffles = int(input("Podaj liczbe randomizacji.\n"))
    graph_seq = gseq.load_sequence()
    adj = gseq.is_graphic_sequence(graph_seq)

    start_incidence = adjacency_matrix_to_incidence_matrix(adj)
    print(np.matrix(start_incidence))

    [is_graphic, randomized_incidence] = randomize_edges(graph_seq, num_shuffles)
    print(np.matrix(randomized_incidence))
    graph = create_igraph_from_incidence_matrix(randomized_incidence)
    plot_igraph_on_circle(graph)
