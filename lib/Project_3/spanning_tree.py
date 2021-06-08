from operator import attrgetter
from matplotlib import pyplot as plt

from lib.Project_3.weighted_graph import plot_two_graphs_in_subplots
from lib.Utils.pretty_print import print_int_matrix


class Edge:
    def __init__(self, vertex_a, vertex_b, weight):
        self.start = vertex_a
        self.end = vertex_b
        self.weight = weight


# returns adjacency matrix of resulting spanning tree.
# returns empty list if finding neighbours fails (graph is not connected).
def prim_generate_minimum_spanning_tree(adjacency_matrix):
    size = len(adjacency_matrix)
    res = [[0] * size for _ in range(size)]

    ready_vertices = [0]
    free_vertices = [i for i in range(1, size)]

    while len(ready_vertices) < size:
        edges = []
        for v in ready_vertices:
            edges += [Edge(v, j, adjacency_matrix[v][j]) for j in range(size) if adjacency_matrix[v][j]]
        available_edges = [e for e in edges if e.end not in ready_vertices]
        if not available_edges:
            return []
        min_edge = min(available_edges, key=attrgetter('weight'))

        res[min_edge.start][min_edge.end] = res[min_edge.end][min_edge.start] = min_edge.weight
        ready_vertices.append(min_edge.end)
        free_vertices.remove(min_edge.end)

    return res


def draw_minimum_spanning_tree(adjacency_matrix, arg_singleton):
    args = arg_singleton.get_instance().arguments
    res_adj_mat = prim_generate_minimum_spanning_tree(adjacency_matrix)
    if not res_adj_mat:
        print('Blad generacji minimalnego drzewa rozpinajacego: graf nie jest spojny.')
        return
    
    if args['plots'] != 'n':
        t1 = 'Oryginalny graf'
        t2 = 'Minimalne drzewo rozpinajace'
        plot_two_graphs_in_subplots(adjacency_matrix, res_adj_mat, t1, t2)

    print('Otrzymano drzewo rozpinajace o macierzy sasiedztwa:')
    print_int_matrix(res_adj_mat)

    s = int(sum([sum(row) for row in res_adj_mat]) / 2)
    print('Suma wag krawedzi drzewa to {}\n'.format(s))
