from igraph import *


def create_digraph_from_adjacency_matrix(matrix):
    g = Graph(directed = True)
    g.add_vertices(len(matrix))

    for row_num, row in enumerate(matrix):
        for col_num, val in enumerate(row):
            if val == 1:
                g.add_edges([(row_num, col_num)])

    return g