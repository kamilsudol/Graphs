import numpy as np

from lib.Project_4.bellman_ford import bellman_ford, get_proper_random_weights
from lib.Project_3.dijkstras import dijkstra_find_shortest_paths
from .plot_digraph_on_circle import plot_digraph_on_circle
from .DiMatrixRepresentation import DiMatrixRepresentation
from lib.Project_1.matrix_conversions import adjacency_matrix_to_list
from lib.Project_1.read_data import print_list
from .random_digraph import generate_random_digraph


def add_s(G, w):
    n = len(G) + 1
    G_prim = np.zeros([n, n], dtype=int)
    w_prim = np.zeros([n, n], dtype=int)
    for v in range(n-1):
        for u in range(len(G[v])):
            G_prim[v][u] = G[v][u]
            w_prim[v][u] = w[v][u]
            G_prim[n-1][u] = 1
    return G_prim, w_prim


def johnson(G, w):
    G_prim, w = add_s(G, w)
    n = len(G_prim)
    G_prim = adjacency_matrix_to_list(G_prim)
    G = adjacency_matrix_to_list(G)
    state, h = bellman_ford(G_prim, w, n)
    w_prim = np.zeros([n, n], dtype=int)
    for v in range(n):
        for u in G_prim[v]:
            w_prim[v][u-1] = w[v][u-1] + h[v] - h[u-1]
    D = np.zeros([n - 1, n - 1], dtype=float)
    for u in range(len(G)):
        du_prim, pu_prim = dijkstra_find_shortest_paths(w_prim, u)
        for v in range(len(G)):
            try:
                D[u][v] = du_prim[v] - h[u] + h[v]
            except OverflowError:
                D[u][v] = np.Inf
    return D


def paths_between_nodes():
    random_graph_adj = generate_random_digraph()
    list_random_graph = adjacency_matrix_to_list(random_graph_adj)
    random_weights = get_proper_random_weights(list_random_graph)

    random_graph_plot = DiMatrixRepresentation.AdjacencyMatrix.to_digraph_func()(random_graph_adj)
    plot_digraph_on_circle(random_graph_plot, weights=[random_graph_adj, random_weights])

    D = johnson(random_graph_adj, random_weights)
    
    print_list(D)