import numpy as np
import random as rnd
from lib.Project_1.matrix_conversions import adjacency_matrix_to_list
from .plot_digraph_on_circle import plot_digraph_on_circle
from .DiMatrixRepresentation import DiMatrixRepresentation
from .random_digraph import random_graph_probability


def get_random_w(list):
    n = len(list)
    random_w = np.zeros([n, n], dtype=int)
    for u in range(n):
        for v in list[u]:
            # random_w[u][v - 1] = rnd.randint(-5, 10)
            random_w[u][v - 1] = rnd.randint(-1, 10)

    return random_w


def bellman_ford(G, w, s):
    s -= 1
    ds = [np.Inf for v in G]
    ps = [0 for v in G]
    ds[s] = 0

    for i in range(1, len(G)):
        for u in range(len(G)):
            for v in G[u]:
                if ds[v - 1] > ds[u] + w[u][v - 1]:
                    ds[v - 1] = ds[u] + w[u][v - 1]
                    ps[v - 1] = u
    for u in range(len(G)):
        for v in G[u]:
            if ds[v - 1] > ds[u] + w[u][v - 1]:
                return False
    return True, ds


def get_proper_random_weights(list_random_graph):
    while True:
        random_weights = get_random_w(list_random_graph)
        try:
            state, ds = bellman_ford(list_random_graph, random_weights, 1)
            break
        except:
            continue
    return random_weights


def bellman_ford_start():
    num_vertices, probability = input(
        "Podaj liczbe wierzcholkow grafu i prawdopodbienstwo istnienia krawedzi\n> ").split()
    num_vertices = int(num_vertices)
    probability = float(probability)

    random_graph_adj = random_graph_probability(num_vertices, probability)

    vert_start = int(input("Podaj numer wierzchołka:"))

    if vert_start - 1 > len(random_graph_adj):
        print("Błędne dane!")
        raise ValueError

    list_random_graph = adjacency_matrix_to_list(random_graph_adj)
    random_weights = get_proper_random_weights(list_random_graph)

    state, ds = bellman_ford(list_random_graph, random_weights, vert_start)

    random_graph_plot = DiMatrixRepresentation.AdjacencyMatrix.to_digraph_func()(random_graph_adj)
    plot_digraph_on_circle(random_graph_plot, weights=[random_graph_adj, random_weights])

    print("Wagi scieżek od wierzchołka {}:".format(vert_start) + str(ds))