import numpy as np
import numpy.lib.recfunctions as recfunctions

import sys
import os
sys.path.append(os.path.abspath('Project 1'))   #hacky, maybe add proper modules and lib directory?

from igraph_creation import create_igraph_from_adjacency_matrix
from plot_igraph_on_circle import plot_igraph_on_circle

def load_sequence():
    sequence_input = input('Wprowadz ciag: ').strip().split(' ')
    return [int(i) for i in sequence_input]

def is_graphic_sequence(seq):
    seq = np.sort(seq)[::-1]
    seq = recfunctions.merge_arrays([seq, range(len(seq))])
    seq.dtype.names = ['neighbors', 'vertex']
    adj_matrix = np.zeros((len(seq), len(seq)))

    while True:
        if np.all(seq['neighbors'] == 0):
            return adj_matrix

        if seq[0]['neighbors'] >= len(seq) or np.any(seq['neighbors'] < 0) or np.count_nonzero(seq['neighbors'] % 2 == 1) % 2 == 1:
            return False

        for i in range(1, seq[0]['neighbors'] + 1):
            seq[i]['neighbors'] -= 1
            adj_matrix[ seq[0]['vertex'] ][ seq[i]['vertex'] ] = adj_matrix[ seq[i]['vertex'] ][ seq[0]['vertex'] ] = 1

        seq[0]['neighbors'] = 0
        seq.sort(order='neighbors')
        seq = seq[::-1]

seq = load_sequence()
res = is_graphic_sequence(seq)

if res is not False:
    print("Ciag jest graficzny")
    graph = create_igraph_from_adjacency_matrix(res)
    plot_igraph_on_circle(graph)
else:
    print("Ciag nie jest graficzny")