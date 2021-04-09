from igraph import *
from .matrix_conversions import list_to_adjacency_matrix


# assume simple graph (matrix symmetric with respect to the diagonal and only zeros on diagonal)
# use upper right part
def create_igraph_from_adjacency_matrix(matrix):
    g = Graph()
    g.add_vertices(len(matrix))
    skip_diagonal = 1

    for row_num, row in enumerate(matrix):
        for col_num, val in enumerate(row[row_num + skip_diagonal:]):
            if val == 1:
                g.add_edges([(row_num, col_num + row_num + skip_diagonal)])

    return g


# assume simple graph (there is no -1 in the matrix and sum of numbers in a column is 2)
def create_igraph_from_incidence_matrix(matrix):
    g = Graph()
    g.add_vertices(len(matrix))

    if len(matrix) == 0:
        raise Exception()

    for col_num in range(len(matrix[0])):
        edge_vertices = []

        for row_num in range(len(matrix)):
            test = matrix[row_num][col_num]
            if matrix[row_num][col_num] == 1:
                edge_vertices.append(row_num)

        if len(edge_vertices) == 2:
            g.add_edges([edge_vertices])

    return g


def create_igraph_from_list(matrix):
    return create_igraph_from_adjacency_matrix(list_to_adjacency_matrix(matrix))
