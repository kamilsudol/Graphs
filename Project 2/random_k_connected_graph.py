import numpy as np
import numpy.lib.recfunctions as recfunctions
import random as rng

import sys
import os
sys.path.append(os.path.abspath('Project 1'))   #hacky, maybe add proper modules and lib directory?

from igraph_creation import create_igraph_from_adjacency_matrix
from plot_igraph_on_circle import plot_igraph_on_circle

def generate_random_k_connected_graph(vertices, k):
    seq = recfunctions.merge_arrays([[k]*vertices, range(vertices)])
    seq.dtype.names = ['neighbors', 'vertex']
    adj_matrix = np.zeros((len(seq), len(seq)))

    for retries in range(100):
        while True:
            if len(seq) == 0:
                return adj_matrix
            elif len(seq) == 1:
                break

            index_from = rng.randint(0, len(seq) - 1)
        
            index_to = rng.randint(0, len(seq) - 1)
            while index_from == index_to or (adj_matrix[ seq[index_from]['vertex'] ][ seq[index_to]['vertex'] ] == 1):
                index_to = rng.randint(0, len(seq) - 1)

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

    return None

def generate_and_show_random_k_connected_graph():
    rng.seed()

    while True:
        vertices, k = [int(i) for i in input("Wprowadz liczbe wierzcholkow i stopien k regularnosci\n> ").strip().split(" ")]
        random_adj = generate_random_k_connected_graph(vertices, k)

        if random_adj is not None:
            graph = create_igraph_from_adjacency_matrix(random_adj)
            plot_igraph_on_circle(graph)
            return
        else:
            print("Nie udalo sie utworzyc grafu\n\n")