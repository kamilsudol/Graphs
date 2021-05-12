from lib.Project_1.igraph_creation import create_igraph_from_adjacency_matrix
from lib.Project_1.plot_igraph_on_circle import plot_igraph_on_circle

import numpy as np
import numpy.lib.recfunctions as recfunctions
import random as rng


def generate_index_not(index_to_avoid, adj_matrix, seq):
    index = rng.randint(0, len(seq) - 1)
    for reretries in range(100):
        if index == index_to_avoid or (adj_matrix[seq[index]['vertex']][seq[index_to_avoid]['vertex']] == 1):
            index = rng.randint(0, len(seq) - 1)
        else:
            return index

    return None


def generate_random_k_connected_graph(vertices, k):
    if vertices*k % 2 == 1:
        return None

    for retries in range(100):
        seq = recfunctions.merge_arrays([[k]*vertices, range(vertices)])
        seq.dtype.names = ['neighbors', 'vertex']
        adj_matrix = np.zeros((len(seq), len(seq)))

        while True:
            if len(seq) == 0:
                print("Ilość prób: " + str(retries + 1))
                return adj_matrix
            elif len(seq) == 1:
                break

            index_from = rng.randint(0, len(seq) - 1)
            index_to = generate_index_not(index_from, adj_matrix, seq)

            if index_to is None:
                break

            adj_matrix[ seq[index_from]['vertex'] ][ seq[index_to]['vertex'] ] = adj_matrix[ seq[index_to]['vertex'] ][ seq[index_from]['vertex'] ] = 1

            if seq[index_from]['neighbors'] == 1:
                seq = np.delete(seq, index_from, 0)
                if index_to > index_from:
                    index_to -= 1
            else:
                seq[index_from]['neighbors'] -= 1

            if seq[index_to]['neighbors'] == 1:
                seq = np.delete(seq, index_to, 0)
            else:
                seq[index_to]['neighbors'] -= 1


    print("Ilość prób: " + str(retries + 1))
    return None

def generate_and_show_random_k_connected_graph(vertices=None, k=None):
    rng.seed()

    while True:
        if vertices is None or k is None: vertices, k = [int(i) for i in input("Wprowadz liczbe wierzcholkow i stopien k regularnosci\n> ").strip().split(" ")]
        random_adj = generate_random_k_connected_graph(vertices, k)

        if random_adj is not None:
            graph = create_igraph_from_adjacency_matrix(random_adj)
            plot_igraph_on_circle(graph)
            return
        else:
            print("Nie udalo sie utworzyc grafu\n\n")
            return