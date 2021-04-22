import lib.Project_2.graphic_sequence as gseq

import random as rng
import numpy as np

from lib.Project_1.matrix_conversions import adjacency_matrix_to_incidence_matrix
from lib.Project_1.igraph_creation import create_igraph_from_incidence_matrix
from lib.Project_1.plot_igraph_on_circle import plot_igraph_on_circle

# Pick two random edges from incidence matrix
# inc -> graph as incidence matrix
# num_vertices -> number of vertices in a graph (number of rows)
# Returns array of data in order edge one column, edge two column, edge one vertices, edge two vertices
def roll_edges(inc, num_vertices):
    rng.seed()

    edge_one_col = -1
    edge_two_col = -1
    edge_one_vertices = [-1, -1]
    edge_two_vertices = [-1, -1]

    # Pick two different edges
    while edge_one_col == edge_two_col or edge_one_vertices[0] == edge_two_vertices[1] or edge_one_vertices[1] == edge_two_vertices[0]:
        edge_one_col = rng.randint(0, num_vertices)
        edge_two_col = rng.randint(0, num_vertices)

        edge_one_vertices = find_vertices(num_vertices, inc, edge_one_col)
        edge_two_vertices = find_vertices(num_vertices, inc, edge_two_col)

    return [edge_one_col, edge_two_col, edge_one_vertices, edge_two_vertices]

# Swaps vertex to another edge
# row -> row index of vertex to be swapped
# col1 -> column index of edge one 
# col2 -> column index of edge two
# matrix -> graph as incidence matrix
def swap_between_columns(row, col1, col2, matrix):
    temp = matrix[row][col1]
    matrix[row][col1] = matrix[row][col2]
    matrix[row][col2] = temp

# Finds vertices in an edge
# num_vertices -> number of vertices (number of rows)
# inc_matrix -> graph as incidence matrix
# edge_index -> column index of an edge
# Returns indices of vertices in an edge as an array [v1, v2] 
def find_vertices(num_vertices, inc_matrix, edge_index):
    vertices = [-1, -1]
    for row in range(num_vertices):
        # If cell in column is a vertex
        if inc_matrix[row][edge_index] == 1:
            # and haven't found vertex one
            if vertices[0] == -1:
                # Save vertex one
                vertices[0] = row
            else:
                # Save vertex two
                vertices[1] = row
    return vertices

# Find adjacency matrix from a graphic sequence and randomize it
# by swapping vertices between edges
# graphic_seq -> graph as graphic sequence
# num_shuffles -> number of vertex shuffles to be executed
# Returns an array as [is_graphic, inc]
# where is_graphic is either True/False
# and inc is the modified incidence matrix 
def randomize_edges(graphic_seq, num_shuffles):
    is_graphic = False
    # Check if graphic sequence is in fact graphic,
    # and if so return the adjacency matrix of that graphic sequence
    adj = gseq.is_graphic_sequence(graphic_seq)

    if adj is not False:
        is_graphic = True
        num_vertices = len(graphic_seq)

        inc = adjacency_matrix_to_incidence_matrix(adj)
        
        for _ in range(num_shuffles):
            edge_one_col, edge_two_col, edge_one_vertices, edge_two_vertices = roll_edges(inc, num_vertices)

            # If vertex one in edges one and two is the same vertex
            if edge_one_vertices[0] == edge_two_vertices[0]:
                # Swap second vertex
                swap_between_columns(edge_one_vertices[1], edge_one_col, edge_two_col, inc)
                swap_between_columns(edge_two_vertices[1], edge_one_col, edge_two_col, inc)
            else:
                # Swap first vertex
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
