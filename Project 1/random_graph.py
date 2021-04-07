import numpy as np
import random as rng


def adj_matrix_init_zero(num_vertices):
    matrix = []

    for i in range(num_vertices):
        matrix.insert(i, [])
        for j in range(num_vertices):
            matrix[i].append(0)

    return matrix


def random_graph_edges(num_vertices, num_edges):
    matrix = adj_matrix_init_zero(num_vertices)
    rng.seed()

    for x in range(num_edges):
        row = rng.randint(1, num_vertices-1)
        col = rng.randint(0, row-1)

        while matrix[row][col] != 0:
            row = rng.randint(1, num_vertices-1)
            col = rng.randint(0, row-1)

        matrix[row][col] = 1
        matrix[col][row] = 1

    return matrix


def random_graph_probability(num_vertices, probability):
    matrix = adj_matrix_init_zero(num_vertices)
    rng.seed()

    for i in range(num_vertices):
        for j in range(i-1):
            if rng.random() <= probability:
                matrix[i][j] = 1
                matrix[j][i] = 1

    return matrix

